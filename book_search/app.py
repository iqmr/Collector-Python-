import requests

def fetch_books(query, start_index, max_results=10):
    """ Fetch books from Google Books API based on the query """
    api_url = (f"https://www.googleapis.com/books/v1/volumes?q="
               f"{query}&startIndex={start_index}&maxResults={max_results}")

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
    start_index = 0
    max_results = 10
    search_term = input("Enter search term: ")
    while True:
        books = fetch_books(query=search_term, start_index=start_index, max_results=max_results)
        if not books.get("items", []):
            print("No results")
        display_books(books)

        next_step = input("Press 'n' for next page of results or any "
                        "other key to exit the app. "
                        ": ")
        if next_step.lower() != "n":
            break
        start_index += max_results
        print()
        print("Pagination number: ", start_index)
        print()





    # title(books)
    # print(books["items"][0]["volumeInfo"]["title"])



if __name__ == "__main__":
    main()

main()

