import streamlit as st

# NEW: Attractive background + styles
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #7b4397, #dc2430);
        background-size: 400% 400%;
        animation: gradientMove 15s ease infinite;
    }
    @keyframes gradientMove {
        0%   {background-position: 0% 50%;}
        50%  {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp li {
        color: #FFFFFF;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }
    .welcome-box {
        text-align: center;
        padding: 25px 15px;
        margin-bottom: 20px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        animation: fadeIn 2s ease;
    }
    .welcome-box h1 {
        font-size: 2.2rem;
        margin: 0;
    }
    .welcome-box p {
        font-size: 1.1rem;
        margin: 8px 0 0 0;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to   {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# NEW: Welcome banner
st.markdown(
    """
    <div class="welcome-box">
        <h1>👋 Welcome to My Profile!</h1>
        <p>Glad you're here. Take a look around ✨</p>
    </div>
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
st.write("• **Email:** johnalbertzbacomo@gmail.com")
st.write("• **Favorite Countries:** Japan 🇯🇵 and Switzerland 🇨🇭")

st.info("Thanks for visiting my profile page!")
st.balloons()  # NEW: balloons pop up when the page opens 🎈
