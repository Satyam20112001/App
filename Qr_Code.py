import streamlit as st

st.set_page_config(page_title="Magic Trick App", layout="centered")

st.title("🎩 Welcome to the Magic Trick Portal")

# Step 1: Get User Name
fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if fname and lname:
    full_name = f"{fname} {lname}"
    st.success(f"Hello Mr. {full_name} 👋")

    # Step 2: Ask to Increase Volume
    st.warning("🔊 Please increase your volume to maximum to proceed.")
    st.audio("https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3")

    volume_check = st.radio("Could you hear the sound clearly?", ["Yes", "No"])
    if volume_check == "No":
        st.error("You must increase the volume to continue. Bye!")
        st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
        st.stop()

    # Step 3: Ask for Magic Trick
    trick = st.radio("Do you want to see a magic trick?", ["Yes", "No"])
    if trick == "No":
        st.error(f"😈 Goodbye Mr. {full_name}! You are kicked out!")
        st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
        st.stop()

    # Step 4: Like Instagram Post
    st.info("🚨 You have to like a post first. Then only we move forward.")

    # ✅ Instagram Styled Button
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
    if liked == "No":
        st.error("Please like the post to proceed.")
        st.stop()

    # Final Step: Show Magic
    st.success("✅ Thanks for liking the post! Now, here's your magic trick 🎩")
    st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
