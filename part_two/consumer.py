import pika
from contact_model import Contact


def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(f'[x] Received object id: {body}')

    # Retrieving contact object from the database
    contact_id = body
    contact = Contact.objects.get(id=contact_id)

    # Sending email
    print(f'Sending a mail to {contact.email}')
    contact.mailed = True
    contact.save()
    print(f'Mail was successfully sent to {contact.fullname}')


def main():
    # Establishing connection to RabbitMQ server
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    # Setting up message consumer
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages')

    # Start consuming messages
    channel.start_consuming()


if __name__ == "__main__":
    main()
