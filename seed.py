import json
from datetime import datetime
from models import Author, Quote
from connect_db import create_connection


def load_authors():
    Author.drop_collection()
    with open('authors.json', 'r', encoding='utf-8') as file:
        authors = json.load(file)
        for i in authors:

            author = Author(
                fullname=i['fullname'],
                born_date=datetime.strptime(i['born_date'], '%B %d, %Y'),
                born_location=i['born_location'],
                description=i['description']
            )

            author.save()


def load_quotes():
    Quote.drop_collection()
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        for q in quotes:

            for a in Author.objects:
                if a.fullname == q['author']:
                    author = a
                    break
            quote = Quote(
                tags=q['tags'],
                author=author,
                quote=q['quote']
            )
            quote.save()


if __name__ == "__main__":
    create_connection()
    load_authors()
    load_quotes()
