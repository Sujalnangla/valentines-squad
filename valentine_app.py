import streamlit as st
import datetime
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Cute Squad Hub", page_icon="🧸", layout="wide")

# --- THEME MANAGEMENT ---
if 'theme' not in st.session_state:
    st.session_state.theme = 'Light'

if st.sidebar.button("🌓 Toggle Dark/Light Mode"):
    st.session_state.theme = 'Dark' if st.session_state.theme == 'Light' else 'Light'

# --- CUSTOM CSS ---
if st.session_state.theme == 'Dark':
    bg_gradient = "linear-gradient(-45deg, #2c3e50, #000000, #434343)"
    card_bg = "rgba(30, 30, 30, 0.95)"
    text_color = "#ecf0f1"
    header_color = "#ff9ff3"
else:
    bg_gradient = "linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #a18cd1)"
    card_bg = "rgba(255, 255, 255, 0.90)"
    text_color = "#2c3e50"
    header_color = "#ff6b6b"

st.markdown(f"""
    <style>
    .stApp {{
        background: {bg_gradient};
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }}
    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    .main-card {{
        background: {card_bg};
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        color: {text_color};
        text-align: center;
        margin-bottom: 20px;
    }}
    h1, h2, h3 {{ color: {header_color} !important; font-family: 'Comic Sans MS', sans-serif; }}
    </style>
    """, unsafe_allow_html=True)

# --- FUNCTION: HEART RAIN ---
def rain_hearts():
    placeholder = st.empty()
    st.markdown("### ❤️💖❤️💖❤️") # Instant visual feedback
    with placeholder.container():
        for _ in range(5):
            left = random.randint(1, 90)
            st.markdown(f"<div style='position: fixed; left: {left}%; top: 10%; font-size: 40px; z-index: 9999;'>💖</div>", unsafe_allow_html=True)
            time.sleep(0.1)
    time.sleep(1)
    placeholder.empty()

# --- DATA ---
ALL_DAYS = {
    "Rose Day": {"date": 7, "img": "https://loremflickr.com/800/600/rose,flower", "quote": "Friends are the flowers of life."},
    "Propose Day": {"date": 8, "img": "https://loremflickr.com/800/600/puppy,cute", "quote": "Besties forever!"},
    "Chocolate Day": {"date": 9, "img": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=800", "quote": "Sweeter than candy."},
    "Teddy Day": {"date": 10, "img": "https://loremflickr.com/800/600/teddybear", "quote": "Bear-y big hugs!"},
    "Promise Day": {"date": 11, "img": "https://loremflickr.com/800/600/holdinghands", "quote": "Pinky promise."},
    "Hug Day": {"date": 12, "img": "https://loremflickr.com/800/600/kitten", "quote": "Huge squeeze!"},
    "Kiss Day": {"date": 13, "img": "https://loremflickr.com/800/600/love,heart", "quote": "Virtual kisses!"},
    "Valentine's Day": {"date": 14, "img": "https://loremflickr.com/800/600/party", "quote": "Happy Palentine's!"}
}

# --- NAVIGATION ---
st.sidebar.title("🧸 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Daily Slides", "Poetry Machine"])

# --- INTERACTIVE HOME PAGE ---
if page == "Home":
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.title("✨ The Squad Headquarters ✨")
    
    # 1. Personal Greeting
    name = st.text_input("Enter your name to unlock the hub:", placeholder="Type your name here...")
    
    if name:
        st.write(f"### Hello, {name}! 👋")
        st.write("Welcome to the most wholesome place on the internet.")
        
        # 2. Vibe Check
        st.markdown("---")
        st.subheader("🌡️ Vibe Check")
        mood = st.select_slider("How are we feeling today?", options=["Sleepy 😴", "Hungry 🍟", "Chill 😎", "Loved 🥰", "Hyper 🤪"])
        
        if mood == "Loved 🥰":
            st.success("Aww! We love you too!")
            rain_hearts()
        elif mood == "Hungry 🍟":
            st.warning("Go grab a snack, bestie!")
        elif mood == "Hyper 🤪":
            st.balloons()

        # 3. Friendship Meter
        st.markdown("---")
        st.subheader("🔋 Friendship Battery")
        friendship_level = st.slider("Rate our squad (be honest!):", 0, 100, 50)
        
        if friendship_level == 100:
            st.success("MAXIMUM FRIENDSHIP ACHIEVED! 🚀")
            rain_hearts()
        elif friendship_level > 80:
            st.info("That's pretty strong!")
        else:
            st.write("C'mon, crank it up!")

    else:
        st.info("👆 Tell us who you are to start the fun!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- DAILY SLIDES PAGE ---
elif page == "Daily Slides":
    today_val = datetime.date.today().day
    visible_days = {k: v for k, v in ALL_DAYS.items() if v["date"] <= min(today_val, 14)}
    
    if not visible_days:
        st.info("Wait for Feb 7th!")
    else:
        day = st.select_slider("Pick a Day", options=list(visible_days.keys()))
        data = visible_days[day]
        col1, col2 = st.columns(2)
        with col1:
            st.image(data["img"], use_container_width=True)
        with col2:
            st.markdown(f"<div class='main-card'><p style='font-size:24px; font-weight:bold;'>\"{data['quote']}\"</p></div>", unsafe_allow_html=True)
            if st.button("Send Love! 💖"):
                rain_hearts()

# --- POETRY PAGE ---
# --- HINDI POETRY PAGE (Eyes & Smile Edition) ---
# --- HINDI POETRY PAGE (With Music & Eyes/Smile Theme) ---
# --- HINDI POETRY PAGE (With YouTube Music) ---
# --- HINDI POETRY PAGE (With Autoplay Music) ---
elif page == "Poetry Machine":
    st.title("📜 The Shayar (Poet)")
    
    # 🎵 AUTOPLAY MUSIC SETUP
    # We add '?autoplay=1' to force start. 
    # Note: Some mobile browsers might still require a click due to privacy settings.
    st.markdown("""
        <div style="text-align:center; margin-bottom: 20px;">
            <iframe width="0" height="0" 
            src="https://www.youtube.com/embed/sK7riqg2mr4?autoplay=1&start=15" 
            frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <p style="font-size: 12px; color: grey;">(🎵 Music should be playing...)</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✨ Mere Dost Ke Liye ✨")
    
    friend_name = st.text_input("Kiske liye shayari likhni hai? (Enter Name):")
    
    if st.button("Generate Shayari 🖋️"):
        if friend_name:
            # ... (Keep your existing Shayari list here) ...
            shayaris = [
                f"Teri muskaan se din khil jaata hai,\nTeri aankhon mein sukoon mil jaata hai,\nJab bhi dekhta hoon {friend_name} tujhe,\nDil ko ek naya saun mil jaata hai. 💖",
                f"Aankhon mein teri chamak sitaaron jaisi,\nMuskaan teri phoolon ki bahaaron jaisi,\n{friend_name}, tu dost hai sabse pyaara,\nTeri dosti hai duniya ke nazaaron jaisi. 🌟",
                f"Na chand ki chahat, na taaron ki farmaish,\nBas teri hansi rahe, yahi hai khwaish,\nJab bhi muskuraye {friend_name} tu,\nLagta hai poori ho gayi har azmaish. 😊",
                f"Teri jhuki nazron mein bhi ek baat hai,\nTeri hansi mein chhipi kayi saugaat hai,\nKhushkismat hoon jo {friend_name} tu mila,\nYeh dosti mere liye sabse khaas hai. 🤝"
            ]
            
            selected_shayari = random.choice(shayaris)
            
            st.markdown(f"""
            <div class='main-card' style='background: linear-gradient(to right, #ffefba, #ffffff); color: #d35400; border-left: 5px solid #e67e22;'>
                <p style='font-size:22px; font-family: "Georgia", serif; font-style:italic; line-height: 1.8;'>
                {selected_shayari.replace(chr(10), '<br>')}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            rain_hearts()
        else:
            st.warning("Naam toh likho pehle! 😉")