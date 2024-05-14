from mongoengine import Document, connect
from mongoengine.fields import StringField, EmailField, BooleanField

connect(db='HW08_part2',
        host=f'mongodb+srv://andrewpechersky:eDc5P7lCgbOS31Qx@cluster0.jylrhmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


class Contact(Document):
    fullname = StringField(max_length=50, required=True)
    email = EmailField(required=True)
    mailed = BooleanField(default=False)