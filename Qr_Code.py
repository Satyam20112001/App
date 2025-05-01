import streamlit as st
import time

st.title("🎩 Welcome to the Satyam Rajput's Portal")

# Step 0: Setup session state
if "audio_played" not in st.session_state:
    st.session_state.audio_played = False
if "volume_ok" not in st.session_state:
    st.session_state.volume_ok = False
if "instagram_clicked" not in st.session_state:
    st.session_state.instagram_clicked = False

# Step 1: Get User Title
title = st.radio("Select your Title", ["Mr.", "Miss", "Mrs.", "Dr."])

# Step 2: Get User Name
fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if fname and lname:
    full_name = f"{title} {fname} {lname}"
    st.success(f"Hello {full_name}, Satyam Welcomes you to his digital portal 👋")

    # Step 3: Prompt to Play Audio
    st.warning("🔊 Please click the button below to play the audio and wait for 5 seconds.")

    if st.button("Play Audio"):
        st.markdown(
            """
            <audio controls autoplay>
              <source src="https://dl.prokerala.com/downloads/ringtones/files/mp3/love-me-like-u-do-23635.mp3">
              Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True
        )
        time.sleep(6.8)
        st.session_state.audio_played = True

    if st.session_state.audio_played:
        st.success("✅ Audio played for 5 seconds. You may proceed.")

        volume_check = st.radio("Could you hear the sound clearly?", ["Yes", "No"], index=None)

        if volume_check == "No":
            st.error("You must increase the volume to proceed.")
            st.stop()
        elif volume_check == "Yes":
            st.session_state.volume_ok = True

    # Proceed only if volume is OK
    if st.session_state.volume_ok:
        st.info("🚨 You have to like a post first. Then only we move forward.")

        # Display Instagram Button after the volume check
        st.markdown(
            """
            <style>
            .insta-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                background-color: #E1306C;
                color: white;
                border: none;
                border-radius: 8px;
                text-decoration: none;
            }
            </style>
            <a href="https://www.instagram.com/reel/DJEzq2HT_UL/?utm_source=ig_web_copy_link" 
               target="_blank" class="insta-button" 
               onclick="window.parent.postMessage('instagram_clicked', '*');">Open Instagram Post</a>
            """,
            unsafe_allow_html=True
        )

        # Track if Instagram Post has been clicked
        if "instagram_clicked" in st.session_state and not st.session_state.instagram_clicked:
            st.session_state.instagram_clicked = True

        liked = st.radio("Have you liked the post?", ["Yes", "No"], index=None)  # Make the default option empty

        # Show content only after the user selects an option
        if liked == "Yes":
            st.markdown(
                """
                <div style="text-align: center; font-size: 28px; font-weight: bold; color: green; margin-top: 30px;">
                    काम खतम अब क्या करना है रुक कर, टाटा-बायबाय! लाइक कर दिया, अब यहा रुक कर क्या देख रहे हो कुछ नहीं मिलेगा! 
                    जा कर पढ़ाई लिखाई करो! IS, YS बनो, और यहा हवा आने दो! 😉 फिर मिलेंगे. जब कोई और 'महान' कार्य संपन्न करना हो!
                </div>
                <div style="text-align: center; margin-top: 30px;">
                    <video width="100%" height="400" autoplay unmuted playsinline loop controls>
                        <source src="https://cdn.jsdelivr.net/gh/Satyam20112001/my-video-assets@main/RPReplay_Final1722203131-1.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                """,
                unsafe_allow_html=True
            )

        elif liked == "No":
            st.markdown(
                """
                <div style="text-align: center; font-size: 36px; font-weight: bold; color: red; margin-top: 50px;">
                    Pehli fursat mai nikal!
                </div>
                <div style="text-align: center; margin-top: 30px;">
                    <img src="https://scrolldroll.com/wp-content/uploads/2021/05/hindustani-bhau-meme-templates-nikal-lavde-pehli-fursat-mein-nikal.jpg" 
                         alt="Pehli Fursat Me Nikal" style="max-width: 100%; height: auto;">
                </div>
                <audio autoplay hidden>
                    <source src="https://cdn.jsdelivr.net/gh/Satyam20112001/my-video-assets@main/Hindustani%20Bhau%20-%20Pehli%20Fursat%20Mein%20Nikal%20meme%20template%20%20No%20gali%20%20%20memes.mp3" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
                """,
                unsafe_allow_html=True
            )
        # Add a message that a response is waiting
        else:
            st.markdown(
                """
                <div style="text-align: center; font-size: 40px; font-weight: bold; color: yellow; margin-top: 50px;">
                    A message is waiting for you!
                </div>
                <div style="text-align: center; margin-top: 30px;">
                    <img src="https://media.giphy.com/media/cIbJ5bBlNLxynVGYzb/giphy.gif" 
                         alt="Looping Message GIF" style="max-width: 100%; height: auto;">
                </div>
                """,
                unsafe_allow_html=True
            )
