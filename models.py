from mongoengine import Document, CASCADE
from mongoengine.fields import (
    StringField,
    DateTimeField,
    ListField,
    ReferenceField
)


class Author(Document):
    fullname = StringField(max_length=30, required=True)
    born_date = DateTimeField()
    born_location = StringField(max_length=150)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField('Author', reverse_delete_rule=CASCADE)
    quote = StringField(required=True)
