import requests

def fetch_books(query):
    """ Fetch books from Google Books API based on the query """
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    response = requests.get(api_url)

    books = response.json()
    return books

def display_books(books):
    for item in books.get("items", []):
        info = item["volumeInfo"]
        title = info.get("title", "No title")
        authors = ', '.join(info.get("authors", ["No Authors"]))
        publisher = info.get("publisher", "No publisher")
        description = info.get("description", "No description")
        print(f"Title of a book: {title}\n"
              f"Authors: {authors}\n"
              f"Publisher {publisher}",
              f"Description: {description}")
        print()


def main():
    search_term = input("Enter the query: ")
    while True:
        books = fetch_books(query=search_term)
        if not books.get("items", []):
            print("No results")
        display_books(books)

        next_step = input("Type quit to exit the program: ")
        if next_step.lower() == "quit":
            break





    # title(books)
    # print(books["items"][0]["volumeInfo"]["title"])



if __name__ == "__main__":
    main()

main()

