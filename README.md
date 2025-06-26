# Collaborative Filtering Book Recommender

This is a **Book Recommendation System** that suggests books to users using two main techniques: **Popularity-Based Filtering** and **Collaborative Filtering**. It demonstrates the application of recommender system logic with real-world datasets and includes a simple web interface built with Flask.

---

## Dataset

- **Source:** [Book Recommendation Dataset – Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
- The dataset includes:
  - `Books.csv`: Book metadata (title, author, publisher)
  - `Users.csv`: User demographic information
  - `Ratings.csv`: User ratings for books
- The dataset was cleaned and filtered for meaningful recommendations (based on minimum number of ratings by users and for books).

---

## Libraries Used

- `pandas`, `numpy` – data manipulation and analysis  
- `sklearn` – building collaborative filtering model (cosine similarity)  
- `flask` – for creating a simple web interface  
- `pickle` – saving and loading precomputed models/data  

---

## Recommendation Techniques

### Popularity-Based Recommender

- Filters books that received **at least 200 ratings**.
- Sorts them by **average rating**.
- Displays the **top 50 most popular books** universally.

### Collaborative Filtering Recommender

- Filters users who rated **150+ books** and books with **50+ ratings**.
- Constructs a user-book matrix and computes **cosine similarity** between users.
- Provides **personalized recommendations** based on similar user behavior.

---

## Pickle Files (Model Artifacts)

The following preprocessed models and data are stored as `.pkl` files and **included in the repo via Git LFS**:

- `top_50_books.pkl` – for popularity-based recommendations  
- `pvt.pkl` – user-book pivot table  
- `similarity.pkl` – cosine similarity matrix  
- `books.pkl` – book metadata used in recommendation display

---

## Web App

A simple Flask-based interface is included:

- The **homepage** shows the top 50 most popular books.
- The **recommendation page** allows users to input a book and receive similar book suggestions.

---

## Notes

- The project uses **Git LFS** to manage large `.pkl` files — make sure Git LFS is installed to access them.
- Further enhancements can include:
  - Using matrix factorization (e.g., SVD)
  - Adding login/user profiles
  - Cloud deployment for public access

---

## Author

- **Ali Shayan** – [GitHub Profile](https://github.com/iamalishayan)

---

Feel free to fork the repo, open issues, or suggest improvements!
