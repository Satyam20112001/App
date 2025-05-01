import streamlit as st
import time

st.title("🎩 Welcome to the Magic Trick Portal")

# Step 1: Get User Name
fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if fname and lname:
    full_name = f"{fname} {lname}"
    st.success(f"Hello Mr. {full_name} 👋")

    # Step 2: Prompt to Play Audio
    st.warning("🔊 Please click the button below to play the audio and wait for 5 seconds.")

    if st.button("Play Audio"):
        # Embed audio using HTML
        st.markdown(
            """
            <audio controls autoplay>
              <source src="https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True
        )
        # Wait for 5 seconds
        time.sleep(5)
        st.success("✅ Audio played for 5 seconds. You may proceed.")

        volume_check = st.radio("Could you hear the sound clearly?", ["Yes", "No"])

        if volume_check == "No":
            st.error("You must increase the volume to proceed.")
            st.stop()
        else:
            st.success("Great! Proceeding to the next step.")

        # Step 3: Instagram Post Interaction
        st.info("🚨 You have to like a post first. Then only we move forward.")

        # Styled Instagram Button
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
               target="_blank" class="insta-button">Open Instagram Post</a>
            """,
            unsafe_allow_html=True
        )

        liked = st.radio("Have you liked the post?", ["Yes", "No"])
        if liked == "Yes":
            st.success("वाह! काम ख़त्म, तो टाटा-बायबाय! लाइक तो मिल ही गया, अब यहां रुकना... सरासर ज़्यादती है! चलिए जनाब, हवा आने दीजिए! 😉 फिर मिलेंगे. जब कोई और 'महान' कार्य संपन्न करना हो!")
        else:
            st.error("Pehli fursat mai nikal!")
            # Embed GIF
            st.markdown(
                """
                <img src="https://media.tenor.com/5R7Y3zK7WZkAAAAC/pehli-fursat-me-nikal.gif" alt="Pehli Fursat Me Nikal" width="300">
                """,
                unsafe_allow_html=True
            )
    else:
        st.stop()
