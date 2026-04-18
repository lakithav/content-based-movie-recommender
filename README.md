# 🎬 NextWatch – Movie Recommendation System

A machine learning-powered movie recommendation web application that suggests similar movies based on user selection. Built using Python, Streamlit, and a similarity-based recommendation algorithm.

---

## 🚀 Features

* 🎥 Recommend movies based on user-selected title
* ⚡ Fast similarity-based recommendations
* 🌐 Interactive web UI using Streamlit
* 🧠 Uses precomputed similarity matrix for efficiency
* 🖼️ Displays movie posters using API integration

---

## 🛠️ Tech Stack

* Frontend/UI: Streamlit
* Backend: Python
* Machine Learning: Cosine Similarity
* Data Processing: Pandas, NumPy
* Model Storage: Pickle
* API: TMDb API (for movie posters)

---


## ⚙️ How It Works

1. Movie dataset is preprocessed and cleaned
2. Features like genres, keywords, cast, and crew are combined
3. Text data is vectorized
4. Cosine similarity is computed between movies
5. When a user selects a movie:

   * The system finds similar movies using similarity scores
   * Top recommendations are displayed

---

## ▶️ Installation & Setup

1. Clone the repository
   [git clone https://github.com/your-username/nextwatch.git](https://github.com/lakithav/content-based-movie-recommender.git)
   cd nextwatch

2. Create virtual environment (optional but recommended)
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the application
   streamlit run web/app.py

---


## 📊 Dataset

Movie dataset sourced from: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 🔗 Demo

Live App: https://content-based-movie-recommender-y3moabtezccbpwnnsd2hsg.streamlit.app/

---

## 📌 Future Improvements

* 🔍 Add search autocomplete
* ⭐ Add user ratings & personalization
* 🧠 Improve recommendation using collaborative filtering
* 📱 Improve mobile responsiveness

---

## 🙌 Acknowledgements

* TMDb API for movie data
* Open-source datasets from Kaggle

---

## 📬 Contact

LinkedIn: https://www.linkedin.com/in/lakitha-viraj-20a853263
