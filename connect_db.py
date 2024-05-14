from mongoengine import connect
import configparser
import certifi

ca = certifi.where()

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongo_pass = config.get('DB', 'PASS')
db_name = config.get('DB', 'DB_NAME')

URI = (
    f'mongodb+srv://andrewpechersky:eDc5P7lCgbOS31Qx@cluster0.jylrhmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
)


def create_connection():
    connect(db=db_name, host=URI, ssl=True)
    print(f'Successfully connected to {db_name}')

