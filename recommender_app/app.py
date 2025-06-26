from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load pickled files
with open('top_50_books.pkl', 'rb') as f:
    popular_books = pickle.load(f)

with open('books.pkl', 'rb') as f:
    books = pickle.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

with open('pvt.pkl', 'rb') as f:
    pvt = pickle.load(f)

def recommend(book_name):
    try:
        book_index = np.where(pvt.index == book_name)[0][0]
        suggestions = sorted(list(enumerate(similarity[book_index])), reverse=True, key=lambda x: x[1])[1:5]

        data = []
        for i in suggestions:
            items = []
            temp = books[books['Book-Title'] == pvt.index[i[0]]].drop_duplicates('Book-Title')
            items.append(temp['Book-Title'].iloc[0])
            items.append(temp['Book-Author'].iloc[0])
            items.append(temp['Image-URL-M'].iloc[0])
            data.append(items)
        
        return data
    except IndexError:
        return None

@app.route('/')
def home():
    if hasattr(popular_books, 'to_dict'):
        books = popular_books.to_dict(orient='records')
    else:
        books = popular_books

    return render_template('index.html', books=books)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend_books():
    recommendations = None
    error = None
    book_name = None
    book_titles = list(pvt.index)  # Pass all book titles for autocomplete

    if request.method == 'POST':
        book_name = request.form.get('book_name')
        if book_name and book_name in pvt.index:
            recommendations = recommend(book_name)
        else:
            error = "Book not found. Please select a valid title from the suggestions."

    return render_template('recommend.html', recommendations=recommendations, error=error, book_name=book_name, book_titles=book_titles)

if __name__ == '__main__':
    app.run(debug=True)