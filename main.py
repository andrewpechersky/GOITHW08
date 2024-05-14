from time import sleep
from mongoengine import DoesNotExist
from connect_db import create_connection
from models import Author, Quote


# Search by name
def search_by_name() -> list | str:
    name = input("Author's name: >- ")
    try:
        author = Author.objects.get(fullname=name)
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    except DoesNotExist:
        return f"No matches found for {name}"


# Search by tag
def search_by_tag() -> list:
    tag = input("Search by tag: >- ")
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]


# Search by two tags
def search_by_tags() -> list:
    tags = input("Search by tags: >- ").split(',')
    quotes_set = set()
    for tag in tags:
        quotes = Quote.objects(tags=tag)
        quotes_set.update([quote.quote for quote in quotes])
    return list(quotes_set)


# Mapping of commands to functions
commands = {
    1: search_by_name,
    2: search_by_tags,
    3: search_by_tag
}


# Main function
def main():
    create_connection()
    while True:
        print(
            "Choose the search option:\n"
            "[1] - Search by name\n"
            "[2] - Search by tags\n"
            "[3] - Search by tag\n"
            "[4] - Exit"
        )
        choice = input(">>> ")
        if choice == "4":
            print("Goodbye!")
            sleep(1)
            break
        try:
            option = int(choice)
            if option in commands:
                print(commands[option]())
            else:
                print("Unknown command, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
