# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Streamlit** that suggests movies similar to a selected movie.  
The app uses **cosine similarity** on movie features and fetches posters using the **TMDB API** for a rich visual experience.

---

## 🚀 Live Demo
https://movie-recommender0system.streamlit.app/


---

## 🧠 How It Works
- User selects a movie from the list
- The system computes similarity scores using a precomputed similarity matrix
- Top similar movies are recommended
- Movie posters are fetched dynamically from **TMDB API**
- Results are displayed in a **card-based grid layout**

---

## ✨ Features
- 🎥 Content-based movie recommendations
- 🖼 Movie posters fetched via TMDB API
- 📊 Precomputed similarity matrix for fast results
- 🎨 Clean, responsive UI with card layout
- 🔐 Secure API key handling using Streamlit Secrets

---

## 🛠 Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **TMDB API**
- **Git LFS** (for large model files)

---

## 📁 Project Structure
```text 
movie-recommender/
│──  app.py
│──  movies.pkl
│──  similarity.pkl
│──  requirements.txt
│──  README.md
│── .gitignore
│── .gitattributes

```
---
## Author
- @Pratham597
