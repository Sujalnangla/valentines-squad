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
