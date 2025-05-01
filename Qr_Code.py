import streamlit as st
import webbrowser

st.title("🎩 Welcome to the Magic Trick Portal")

# Name Input
fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if fname and lname:
    full_name = f"{fname} {lname}"
    st.success(f"Hello Mr. {full_name} 👋")

    # Ask user to increase volume
    st.warning("Please increase your volume to maximum to proceed.")
    st.audio("https://yourhost.com/path-to-test-sound.mp3")
    volume_check = st.radio("Could you hear the sound clearly?", ["Yes", "No"])
    if volume_check == "No":
        st.error("You must increase the volume to proceed.")
        st.stop()

    # Ask for magic trick
    choice = st.radio("Do you want to see a magic trick?", ["Yes", "No"])
    if choice == "No":
        st.video("https://yourhost.com/path-to-kickout-animation.mp4")
        st.stop()

    # Instagram post requirement
    st.info("You have to like this Instagram post first. Then only we move forward.")
    if st.markdown(
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
    <a href="https://www.instagram.com/reel/DJEzq2HT_UL/?utm_source=ig_web_copy_link" target="_blank" class="insta-button">Open Instagram Post</a>
    """,
    unsafe_allow_html=True);
    
    liked = st.radio("Have you liked the post?", ["Yes", "No"])
    if liked == "No":
        st.warning("Please like the post to proceed.")
        st.stop()

    # Final magic trick
    st.success("Thanks for the like! Now, here's your magic trick 🎩")
    st.video("https://yourhost.com/path-to-magic-trick.mp4")
