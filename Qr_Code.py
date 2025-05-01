import streamlit as st
import webbrowser
import time
from PIL import Image

# Load animations (GIFs or images)
horror_image = "https://media.giphy.com/media/3o7TKP9xTuj7kTtQ3W/giphy.gif"
kickout_image = "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"
magic_image = "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"

st.set_page_config(page_title="Magic Trick App", layout="centered")
st.title("🎩 Welcome to the Magic Trick Portal")

# 1. Name Input
fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if fname and lname:
    full_name = f"{fname} {lname}"
    st.success(f"Hello Mr. {full_name}, Welcome to Satyam Rajput Digital world 👋")

    # 2. Ask for volume
    st.warning("Please increase your volume to proceed. If you don't, we can't continue.")
    vol = st.radio("Did you increase your volume?", ["Yes", "No"])

    if vol == "No":
        st.image(kickout_image, caption="You're being kicked out! 👋")
        st.stop()

    # 3. Ask to see magic trick
    choice = st.radio("Do you want to see a magic trick?", ["Yes", "No"])

    if choice == "No":
        st.image(kickout_image, caption="Goodbye Mr. {}! Come back for the magic.".format(fname))
        st.stop()

    # 4. Like Instagram to proceed
    st.info("You have to like this Instagram post first. Then only we move forward.")
    ig_clicked = st.button("Open Instagram Post")

    if ig_clicked:
        webbrowser.open_new_tab("https://www.instagram.com/reel/DJEzq2HT_UL/?utm_source=ig_web_copy_link")
        st.success("Thanks for the like! Now, here's your magic trick 🎩")
        st.image(magic_image, caption="✨ Enjoy the magic ✨")

    show_horror = st.checkbox("I don't want to like it")
    if show_horror:
        st.error("You were warned... 😈")
        st.image(horror_image, caption="👻 Gotcha!")
