import pika
from faker import Faker
from contact_model import Contact

# Establishing connection to RabbitMQ server
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

# Creating fake data and sending messages
fake = Faker()
for _ in range(20):
    fullname = fake.name()
    email = fake.email()

    # Creating and saving contact
    contact = Contact(fullname=fullname, email=email)
    contact.save()

    # Publishing contact id to the message queue
    channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id))
    print('Message was successfully sent')

# Closing the connection
connection.close()