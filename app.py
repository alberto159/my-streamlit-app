import os
import random
import streamlit as st

st.set_page_config(page_title="John's Profile", page_icon="🌟")

# ---------- STYLES ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    /* Matte black background */
    .stApp {
        background: #121212;
    }
    .stApp, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp li, .stApp label {
        color: #FFFFFF;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Minecraft buttons */
    div.stButton > button {
        font-family: 'Press Start 2P', monospace;
        font-size: 0.7rem;
        color: #FFFFFF;
        background: #7d7d7d;
        border: 3px solid #000000;
        border-radius: 0;
        padding: 14px 18px;
        text-shadow: 2px 2px 0 #3e3e3e;
        box-shadow: inset -4px -4px 0 #555555, inset 4px 4px 0 #bdbdbd;
    }
    div.stButton > button p {
        font-family: 'Press Start 2P', monospace;
        font-size: 0.7rem;
        color: #FFFFFF;
    }
    div.stButton > button:hover {
        background: #7b8bb5;
        color: #FFFFA0;
        border: 3px solid #FFFFFF;
    }
    div.stButton > button:hover p {
        color: #FFFFA0;
    }
    div.stButton > button:active {
        box-shadow: inset 4px 4px 0 #555555, inset -4px -4px 0 #bdbdbd;
    }

    /* Menu as Minecraft buttons */
    div[role="radiogroup"] {
        gap: 8px;
    }
    div[role="radiogroup"] label {
        background: #7d7d7d;
        border: 3px solid #000000;
        border-radius: 0;
        padding: 10px 12px;
        box-shadow: inset -4px -4px 0 #555555, inset 4px 4px 0 #bdbdbd;
        cursor: pointer;
    }
    div[role="radiogroup"] label > div:first-child {
        display: none;
    }
    div[role="radiogroup"] label p {
        font-family: 'Press Start 2P', monospace;
        font-size: 0.6rem;
        color: #FFFFFF;
        text-shadow: 2px 2px 0 #3e3e3e;
    }
    div[role="radiogroup"] label:hover {
        background: #7b8bb5;
    }
    div[role="radiogroup"] label:has(input:checked) {
        background: #5b8731;
        border: 3px solid #FFFFFF;
        box-shadow: inset -4px -4px 0 #3b5b1f, inset 4px 4px 0 #8bc34a;
    }

    /* Number input */
    div[data-baseweb="input"], div[data-baseweb="input"] input,
    div[data-baseweb="base-input"] {
        background: #2b2b2b !important;
        color: #FFFFFF !important;
        border-radius: 0 !important;
    }
    div[data-testid="stNumberInput"] button {
        background: #7d7d7d;
        color: #FFFFFF;
        border-radius: 0;
    }

    /* Info / alert boxes */
    div[data-testid="stAlert"] {
        background: #1f1f1f;
        border: 2px solid #7d7d7d;
        border-radius: 0;
    }
    div[data-testid="stAlert"] * {
        color: #FFFFFF !important;
    }

    .welcome-box {
        text-align: center;
        padding: 25px 15px;
        margin-bottom: 20px;
        border-radius: 0;
        background: #1f1f1f;
        border: 3px solid #7d7d7d;
        animation: fadeIn 2s ease;
    }
    .welcome-box h1 { font-size: 2.2rem; margin: 0; }
    .welcome-box p { font-size: 1.1rem; margin: 8px 0 0 0; }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to   {opacity: 1; transform: translateY(0);}
    }

    /* NEW: intro card */
    .intro-box {
        padding: 18px 16px;
        margin: 15px 0;
        background: #1f1f1f;
        border: 3px solid #7d7d7d;
        border-left: 6px solid #5b8731;
        border-radius: 0;
    }
    .intro-box p {
        font-size: 1rem;
        line-height: 1.7;
        margin: 0 0 14px 0;
    }
    .intro-box p:last-child { margin-bottom: 0; }

    .meme {
        text-align: center;
        padding: 20px 10px;
        border-radius: 0;
        background: #1f1f1f;
        border: 3px solid #7d7d7d;
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

    # NEW: your introduction
    st.markdown(
        """
        <div class="intro-box">
            <p>👋 Hi guys, welcome to the app! As you can see at the top of my profile, my name is <b>John Albert Z. Bacomo</b>.</p>
            <p>🎓 Currently, I'm a second-year irregular college student 🥲 pursuing <b>Mechanical Engineering (BSME)</b> at <b>North Eastern Mindanao State University (NEMSU)</b>.</p>
            <p>⚙️ I chose Mechanical Engineering because I consider it one of the most versatile branches of engineering, offering a broader scope than many other disciplines. I'm also curious about how machines work and what mechanical work entails, as well as how programming and coding fit into what we work on today.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
