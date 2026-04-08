#  Book Recommendation System (50 Books)

books = {
    # Fantasy 
    "harry potter": {"genre": ["fantasy"], "author": "jk rowling"},
    "lord of the rings": {"genre": ["fantasy"], "author": "jrr tolkien"},
    "the hobbit": {"genre": ["fantasy"], "author": "jrr tolkien"},
    "game of thrones": {"genre": ["fantasy"], "author": "george rr martin"},
    "clash of kings": {"genre": ["fantasy"], "author": "george rr martin"},
    "storm of swords": {"genre": ["fantasy"], "author": "george rr martin"},
    "wheel of time": {"genre": ["fantasy"], "author": "robert jordan"},
    "name of the wind": {"genre": ["fantasy"], "author": "patrick rothfuss"},
    "eragon": {"genre": ["fantasy"], "author": "christopher paolini"},
    "the witcher": {"genre": ["fantasy"], "author": "andrzej sapkowski"},

    # Romance 
    "pride and prejudice": {"genre": ["romance"], "author": "jane austen"},
    "the notebook": {"genre": ["romance"], "author": "nicholas sparks"},
    "fault in our stars": {"genre": ["romance"], "author": "john green"},
    "me before you": {"genre": ["romance"], "author": "jojo moyes"},
    "love story": {"genre": ["romance"], "author": "erich segal"},
    "it ends with us": {"genre": ["romance"], "author": "colleen hoover"},
    "ugly love": {"genre": ["romance"], "author": "colleen hoover"},
    "reminders of him": {"genre": ["romance"], "author": "colleen hoover"},
    "verity": {"genre": ["romance", "thriller"], "author": "colleen hoover"},
    "twilight": {"genre": ["romance", "fantasy"], "author": "stephenie meyer"},

    # Thriller 
    "gone girl": {"genre": ["thriller"], "author": "gillian flynn"},
    "girl with dragon tattoo": {"genre": ["thriller"], "author": "stieg larsson"},
    "da vinci code": {"genre": ["thriller"], "author": "dan brown"},
    "angels and demons": {"genre": ["thriller"], "author": "dan brown"},
    "inferno": {"genre": ["thriller"], "author": "dan brown"},
    "silent patient": {"genre": ["thriller"], "author": "alex michaelides"},
    "behind closed doors": {"genre": ["thriller"], "author": "ba paris"},
    "the guest list": {"genre": ["thriller"], "author": "lucy foley"},
    "sharp objects": {"genre": ["thriller"], "author": "gillian flynn"},
    "dark places": {"genre": ["thriller"], "author": "gillian flynn"},

    # Self-help 
    "atomic habits": {"genre": ["self-help"], "author": "james clear"},
    "rich dad poor dad": {"genre": ["finance"], "author": "robert kiyosaki"},
    "think and grow rich": {"genre": ["finance"], "author": "napoleon hill"},
    "power of now": {"genre": ["self-help"], "author": "eckhart tolle"},
    "subtle art": {"genre": ["self-help"], "author": "mark manson"},
    "deep work": {"genre": ["self-help"], "author": "cal newport"},
    "7 habits": {"genre": ["self-help"], "author": "stephen covey"},
    "ikigai": {"genre": ["self-help"], "author": "hector garcia"},
    "psychology of money": {"genre": ["finance"], "author": "morgan housel"},
    "richest man in babylon": {"genre": ["finance"], "author": "george clason"},

    # Sci-fi 
    "dune": {"genre": ["sci-fi"], "author": "frank herbert"},
    "foundation": {"genre": ["sci-fi"], "author": "isaac asimov"},
    "neuromancer": {"genre": ["sci-fi"], "author": "william gibson"},
    "snow crash": {"genre": ["sci-fi"], "author": "neal stephenson"},
    "ready player one": {"genre": ["sci-fi"], "author": "ernest cline"},
    "enders game": {"genre": ["sci-fi"], "author": "orson scott card"},
    "martian": {"genre": ["sci-fi"], "author": "andy weir"},
    "project hail mary": {"genre": ["sci-fi"], "author": "andy weir"},
    "dark matter": {"genre": ["sci-fi"], "author": "blake crouch"},
    "recursion": {"genre": ["sci-fi"], "author": "blake crouch"}
}

# Book recommendation
def recommend_by_book(book):
    book = book.lower()
    if book not in books:
        return [" Book not found"]

    target = books[book]["genre"]
    return [b for b, data in books.items()
            if b != book and any(g in data["genre"] for g in target)]


# Genre recommendation
def clean_text(text):
    return text.lower().replace("-", " ").strip()


def recommend_by_genre(genre):
    genre = clean_text(genre)

    results = []

    for book, data in books.items():
        for g in data["genre"]:
            if genre == clean_text(g):
                results.append(book)

    return results if results else [" No books found"]

#  Author recommendation
def recommend_by_author(author):
    author = author.lower()

    # Step 1: Find books by author
    author_books = [b for b, data in books.items() if author in data["author"]]

    
    if len(author_books) > 1:
        return author_books

    
    elif len(author_books) == 1:
        book = author_books[0]
        genre = books[book]["genre"]

        recommendations = [b for b, data in books.items()
                           if b != book and any(g in data["genre"] for g in genre)]

        return author_books + recommendations[:5]

    
    else:
        return [" No books found"]



print("Book Recommendation System")

while True:
    print("\n1. Search by Book")
    print("2. Search by Genre")
    print("3. Search by Author")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Enter book name: ")
        results = recommend_by_book(user)

    elif choice == "2":
        user = input("Enter genre: ")
        results = recommend_by_genre(user)

    elif choice == "3":
        user = input("Enter author: ")
        results = recommend_by_author(user)

    elif choice == "4":
        print("Goodbye! ")
        break

    else:
        print("Invalid choice!")
        continue

    print("\nRecommended Books:")
    for r in results:
        print("_", r)
