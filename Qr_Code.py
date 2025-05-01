import streamlit as st

st.title("🎩 Welcome to the Magic Trick Portal")

# Name Input
fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if fname and lname:
    full_name = f"{fname} {lname}"
    st.success(f"Hello Mr. {full_name} 👋")

    # Volume Check
    st.audio("https://yourcdn.com/path-to-test-sound.mp3")
    volume_check = st.radio("Could you hear the sound?", ["Yes", "No"])
    if volume_check == "No":
        st.warning("Please increase your volume to proceed.")
        st.stop()

    # Magic Trick Prompt
    choice = st.radio("Do you want to see a magic trick?", ["Yes", "No"])
    if choice == "No":
        st.video("https://yourcdn.com/path-to-kickout-video.mp4")
        st.stop()

    # Instagram Post Requirement
    st.info("You have to like this Instagram post first. Then only we move forward.")
    st.button(
        '<a href="https://www.instagram.com/reel/DJEzq2HT_UL/?utm_source=ig_web_copy_link" target="_blank">Open Instagram Post</a>',
        unsafe_allow_html=True
    )
    liked = st.radio("Have you liked the post?", ["Yes", "No"])
    if liked == "No":
        st.warning("Please like the post to proceed.")
        st.stop()

    # Display Magic Trick
    st.success("Thanks for the like! Now, here's your magic trick 🎩")
    st.video("https://yourcdn.com/path-to-magic-trick-video.mp4")
