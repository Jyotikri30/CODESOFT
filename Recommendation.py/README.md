Book Recommendation System

 Overview

This project is a simple **Book Recommendation System** built using Python.
It suggests books to users based on their preferences such as **genre, author, or a specific book**.

The main goal of this project is to understand how recommendation systems work using a **content-based filtering approach**.



 Features

 **Search by Book Name**
  Get similar book recommendations based on genre.

 **Search by Genre**
  Enter a genre (like *fantasy, romance, sci-fi*) and get related books.

 **Search by Author**
  Find books written by a specific author.

 **Smart Recommendation Logic**
  If an author has only one book, the system suggests similar books based on genre.

 **User-Friendly Input Handling**
  Handles variations like:

  . "sci-fi" / "sci fi"
  . "self-help" / "self help"



 How It Works

This system uses a **content-based filtering technique**, where each book is defined by its features like **genre and author**.

. When a user selects a book → it recommends books with similar genres
. When a user selects a genre → it returns all books in that category
. When a user selects an author → it shows their books (or similar ones if limited)



 Technologies Used

. Python
. Basic Data Structures (Dictionary, Lists)



 How to Run

1. Open terminal in your project folder
2. Run the file:

```bash
python book_recommender.py


3. Choose an option:

   . Search by book
   .  Search by genre
   . Search by author



 Dataset

The system includes **50 popular books** from different categories:

. Fantasy
. Romance
. Thriller
. Self-help / Finance
. Sci-fi



 Learning Outcome

Through this project, I learned:

. How recommendation systems work
. Difference between rule-based and content-based systems
. Handling user input and edge cases
. Writing clean and structured Python code



 Future Improvements

. Add GUI interface
. Expand dataset (100+ books)
. Use machine learning techniques (TF-IDF, similarity models)
. Add user rating system



 Conclusion

This project is a beginner-friendly implementation of a recommendation system.
It helped me understand the core idea behind how platforms suggest content based on user preferences.



Thank you for checking out this project!
