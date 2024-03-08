import streamlit as st
import subprocess

# Streamlit app UI
st.title("Draw and Guess 🎨✏️")

# Textual statements about the app
st.write("Welcome to Draw and Guess! 🤖💡")
st.write("This app allows you to draw a digit and then predicts what it is. 🎮🕹️")
st.write("Get started by clicking the 'Start Drawing' button below and follow the instructions on the sidebar. 🔢🖼️")

# Instructions for the user
st.sidebar.title("Instructions")
st.sidebar.write("1. Click the 'Start Drawing' button to begin.")
st.sidebar.write("2. A Pygame window will open where you can draw a digit.")
st.sidebar.write("3. Once you've drawn a digit, click the 'Classify' button in the Pygame window to see the prediction.")
st.sidebar.write("4. You can reset the drawing at any time by clicking the 'Reset' button in the Pygame window.")
st.sidebar.write("5. For better performance, it's recommended to use mouse clicks for RESET and CLASSIFY buttons in the Pygame window.")

# Button to start drawing
start_button = st.button("Start Drawing 🖌️")

if start_button:
    # Execute the Pygame script
    subprocess.Popen(["python", "recognition.py", "model.h5"])
    
    # Footer statements
    st.write("---")
    st.write("Made By **_Jaweria Batool_**")
    st.write("For more information about how the app works, please check out the [GitHub README](https://github.com/Jaweria-B/digit-recognition-app) file.")


