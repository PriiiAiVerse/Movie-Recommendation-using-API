## 📅 Project Details

- **Created on**: September 24, 2024
- **Focus**: Rapid prototyping of a recommendation engine using NLP and vector similarity

  ---

🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, scikit-learn, and Streamlit. It uses textual metadata like cast, crew, genre, and plot keywords to recommend movies similar to a user-selected title.

📸 Project Preview

##  🚀 Features

1. Recommends top 5 similar movies using content similarity

2. Simple, user-friendly Streamlit web interface

3. Uses TMDb API to fetch movie posters dynamically

4. Optimized for speed with precomputed .pkl files

5. Real-time search from a dropdown or text input

   ---

##  🧠 How It Works

🔹 Dataset

Files used:

1. tmdb_5000_movies.csv

2. tmdb_5000_credits.csv

These two datasets were merged using the title column to enrich movie metadata.

🔹 Preprocessing Steps

- Data Cleaning: Removed nulls and duplicates.

- Metadata Extraction: Extracted key features from:

cast 

crew

genres

keywords

overview

🔹 Feature Engineering:

- Combined the above features into a new tags column.

- Normalized text (lowercase, tokenized, etc.).

🔹 Vectorization

- Used CountVectorizer to convert tags into vectors (bag-of-words).

- Limited to top 5000 words (excluding English stopwords).

🔹 Similarity Calculation

- Computed cosine similarity across all movie vectors.

- Stored similarity matrix in similarity.pkl.

##   🧰 Tech Stack

| Tool             | Role                            |
| ---------------- | ------------------------------- |
| **Python**       | Core programming language       |
| **Pandas**       | Data manipulation               |
| **scikit-learn** | NLP & similarity computation    |
| **Streamlit**    | Web interface                   |
| **TMDb API**     | Poster/image retrieval          |
| **pickle**       | Save and load preprocessed data |

---


##   💻 Usage

1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```
2. Install Dependencies
```bash

pip install -r requirements.txt
```

3. Setup .env for TMDb API
   
Create a .env file in the root directory:

```env
TMDB_API_KEY=your_tmdb_api_key
```

4. Run the App
```bash

streamlit run app.py
```

----


##  📦 Files and Structure

```bash
Copy
.
├── app.py                   # Streamlit app interface
├── xyz.ipynb                # used for data manipulation
├── movie_dict.pkl           # Serialized movie metadata dictionary
├── similarity.pkl           # Precomputed cosine similarity matrix
├── tmdb_5000_movies.csv     # Raw movie dataset
├── tmdb_5000_credits.csv    # Raw credits dataset
├── README.md                # This file
└── .env                     # API key (excluded from Git)

```

##  🎯 Example Recommendations

If you choose The Dark Knight Rises, the app might recommend:

- The Dark Knight

- Batman Begins

- Batman Returns

- Batman Forever

- Batman

- ---

## 🔐 Security Note

Never share your API key publicly. Use .env files and tools like python-dotenv to keep your keys secure.


## 🧠 Future Improvements

1. Add hybrid recommendations (e.g., collaborative filtering)

2. Integrate genre filters

3. Improve UI with advanced Streamlit components

   ---

🙋‍♀️ Author  :  Priti Kumari


🌟 Show Your Support
If you like this project, consider giving it a ⭐ on GitHub or sharing it with your network.
