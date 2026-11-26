import os
import random
import streamlit as st

st.set_page_config(page_title="John's Profile", page_icon="🌟")

# ---------- STYLES ----------
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
    .stApp, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp li, .stApp label {
        color: #FFFFFF;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }

    div[data-testid="stAlert"] {
        background: rgba(0, 0, 0, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 12px;
    }
    div[data-testid="stAlert"] * {
        color: #FFFFFF !important;
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
    .welcome-box h1 { font-size: 2.2rem; margin: 0; }
    .welcome-box p { font-size: 1.1rem; margin: 8px 0 0 0; }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to   {opacity: 1; transform: translateY(0);}
    }

    .meme {
        text-align: center;
        padding: 20px 10px;
        border-radius: 16px;
        background: #222;
        border: 3px solid #fff;
    }
    .meme-text {
        font-family: Impact, "Arial Black", sans-serif;
        font-size: 1.6rem;
        text-transform: uppercase;
        color: #fff !important;
        text-shadow: 2px 2px 0 #000, -2px -2px 0 #000,
                     2px -2px 0 #000, -2px 2px 0 #000;
        margin: 10px 0;
    }
    .meme-emoji { font-size: 5rem; margin: 10px 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- MENU ----------
page = st.radio(
    "Menu",
    ["🏠 About Me", "🎮 Game", "😂 Coding Meme"],
    horizontal=True,
    label_visibility="collapsed",
)

# =====================================================
# PAGE 1: ABOUT ME
# =====================================================
if page == "🏠 About Me":
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

    st.divider()
    st.subheader("My Hobbies 🏞️")
    st.write("• 🏃 **Running** – chasing new distances")
    st.write("• 🥾 **Hiking** – exploring mountains and trails")
    st.write("• 🎣 **Fishing** – relaxing by the water")

    st.info("Thanks for visiting my profile page!")

# =====================================================
# PAGE 2: GAME
# =====================================================
elif page == "🎮 Game":
    st.header("🎮 Guess the Number!")
    st.write("I'm thinking of a number from **1 to 20**. Can you guess it?")

    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 20)
        st.session_state.tries = 0
        st.session_state.won = False

    guess = st.number_input("Your guess:", min_value=1, max_value=20, value=10, step=1)

    if st.button("Guess! 🎯") and not st.session_state.won:
        st.session_state.tries += 1
        if guess < st.session_state.secret:
            st.warning("📈 Too low! Try higher.")
        elif guess > st.session_state.secret:
            st.warning("📉 Too high! Try lower.")
        else:
            st.session_state.won = True
            st.success(f"🎉 You got it in {st.session_state.tries} tries!")
            st.balloons()

    st.write(f"Tries so far: **{st.session_state.tries}**")

    if st.button("🔄 New Game"):
        st.session_state.secret = random.randint(1, 20)
        st.session_state.tries = 0
        st.session_state.won = False
        st.rerun()

# =====================================================
# PAGE 3: CODING MEME
# =====================================================
elif page == "😂 Coding Meme":
    st.header("😂 Coding Memes")

    # Your meme video
    VIDEO_FILE = "ssstik.io_1795686037703.mp4"
    if os.path.exists(VIDEO_FILE):
        st.video(VIDEO_FILE)
    else:
        st.warning(f"Video '{VIDEO_FILE}' not found. Upload it to GitHub next to app.py.")

    st.divider()

    memes = [
        ("It works on my machine", "🤷‍♂️", "Then we'll ship your machine"),
        ("Me: writes 5 lines of code", "😎", "Bug: 'Error on line 500'"),
        ("Fixing one bug", "🐛", "Creates 3 new bugs"),
        ("Code worked yesterday", "😭", "I changed nothing today"),
        ("Googling the error", "🧑‍💻", "Senior dev = Stack Overflow"),
    ]

    if "meme_i" not in st.session_state:
        st.session_state.meme_i = 0

    top, emoji, bottom = memes[st.session_state.meme_i]

    st.markdown(
        f"""
        <div class="meme">
            <div class="meme-text">{top}</div>
            <div class="meme-emoji">{emoji}</div>
            <div class="meme-text">{bottom}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Next meme 🔄"):
        st.session_state.meme_i = (st.session_state.meme_i + 1) % len(memes)
        st.rerun()
