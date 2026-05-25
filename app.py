import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("netflix_content.csv")


# Must be the first Streamlit command in your script
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Netflix_icon.svg/500px-Netflix_icon.svg.png"
)

# Custom Netflix theme styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000; /* Pure black background */
        color: white;
    }
    h1 {
        color: #E50914; /* Netflix red */
        font-family: Arial, sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #333;
        color: white;
        border: 1px solid #E50914;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with logo + title aligned using Streamlit columns
col1, col2 = st.columns([1, 5])
with col1:
    st.image("netflix_logo.png", width=220) 
with col2:
    st.markdown("<h1>Netflix Recommendation System</h1>", unsafe_allow_html=True)

# User input
movie = st.text_input("Enter a show/movie title:")

if movie:
    st.write(f"Recommendations similar to **{movie}**:")

    # Example: simple content-based recommendation
    recs = df[df['Title'].str.contains(movie.split()[0], case=False)].head(5)

    # Show table only (chart removed)
    st.table(recs[['Title', 'Language Indicator', 'Content Type', 'Hours Viewed']])
