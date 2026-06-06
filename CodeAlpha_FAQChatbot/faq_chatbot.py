import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_data = {
    "What is AI?": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that learns from data.",
    "What is Deep Learning?": "Deep Learning uses neural networks with multiple layers.",
    "What is Python?": "Python is a popular programming language.",
    "What is Data Science?": "Data Science extracts insights from data.",
    "What is NLP?": "Natural Language Processing helps computers understand language.",
    "What is Computer Vision?": "Computer Vision enables machines to interpret images and videos.",
    "What is a Dataset?": "A dataset is a collection of data used for analysis or training.",
    "What is Supervised Learning?": "Learning using labeled data.",
    "What is Unsupervised Learning?": "Learning patterns from unlabeled data.",
    "What is Reinforcement Learning?": "Learning through rewards and penalties.",
    "What is a Neural Network?": "A model inspired by the human brain.",
    "What is Scikit-learn?": "A Python library for machine learning.",
    "What is Pandas?": "A Python library for data manipulation.",
    "What is TensorFlow?": "A deep learning framework developed by Google."
}

questions = list(faq_data.keys())

st.title("FAQ Chatbot")

user_question = st.text_input("Ask a Question")

if st.button("Get Answer"):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        questions + [user_question]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    index = similarity.argmax()

    answer = faq_data[questions[index]]

    st.success(answer)