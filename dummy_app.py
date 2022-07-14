# please be aware that this is a copy from https://github.com/streamlit/theming-showcase
import streamlit as st
import numpy as np


st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/artist-palette_1f3a8.png",
    width=100,
)

"""
# Try out Theming and Widgets!
You can add make a custom theme by updating `.streamlit/config.toml` file.
"""

# Dummy app
def draw_all(
    key,
    plot=False,
):
    st.write(
        """
        ### Example Widgets
        
        These widgets don't do anything. But look at all the new colors they got 👀 
        """
    )

    st.checkbox("Is this cool or what?", key=key)
    st.radio(
        "How many balloons?",
        ["1 balloon 🎈", "2 balloons 🎈🎈", "3 balloons 🎈🎈🎈"],
        key=key,
    )
    st.button("🤡 Click me", key=key)


    st.file_uploader("You can now upload with style", key=key)
    st.slider(
        "From 10 to 11, how cool are themes?", min_value=10, max_value=11, key=key
    )

    st.number_input("So many numbers", key=key)
    st.text_area("A little writing space for you :)", key=key)
    st.selectbox(
        "My favorite thing in the world is...",
        ["Streamlit", "Theming", "Baloooons 🎈 "],
        key=key,
    )

    with st.beta_expander("Expand me!"):
        st.write("Hey there! Nothing to see here 👀 ")
    st.write("")

    if plot:
        st.write("And here's some data and plots")
        st.json({"data": [1, 2, 3, 4]})
        st.dataframe({"data": [1, 2, 3, 4]})
        st.table({"data": [1, 2, 3, 4]})
        st.line_chart({"data": [1, 2, 3, 4]})
        # st.help(st.write)
    st.write("This is the end. Have fun building themes!")


draw_all("main", plot=True)

with st.sidebar:
    draw_all("sidebar")