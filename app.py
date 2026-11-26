import streamlit as st

# NEW: Background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #DDEBFF;
    }
    .stApp, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp li {
        color: #1B1B1B;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.header("John Albert Z. Bacomo")
st.image("IMG_20261126_093653.jpg", width=180)
st.write("Welcome to my Streamlit application!")

st.divider()
st.subheader("About Me")
st.write("• **Course:** BSME Student at NEMSU")
st.write("• **Interests:** Coding, Running, and Drawing")

# NEW: More information
st.write("• **Email:** johnalbertzbacomo@gmail.com")
st.write("• **Favorite Countries:** Japan 🇯🇵 and Switzerland 🇨🇭")

st.info("Thanks for visiting my profile page!")
