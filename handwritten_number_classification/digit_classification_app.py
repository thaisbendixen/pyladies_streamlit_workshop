import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas # https://github.com/andfanilo/streamlit-drawable-canvas

st.markdown('<style>body{color: White; background-color: DarkSlateGrey}</style>', unsafe_allow_html=True)

st.title('My Digit Recognizer')
st.markdown('''Try to write a digit!''')

stroke_width = st.sidebar.slider("Stroke width: ", 1, 100, 25)

SIZE = 192
# this is the drawing canvas
canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=stroke_width,
    stroke_color='#FFFFFF',
    background_color='#000000',
    width=SIZE,
    height=SIZE,
    drawing_mode="freedraw",
    key='canvas')

# this is the output of the drawing canvas rescaled and processed for our model
if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28)) # needs to match the arrays of the digits that were used for training
    rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST) 
    st.write('Rescaled model input')
    st.image(rescaled)

if st.button('Predict'):
    model = load_model('handwritten_number_classification/digit_classifier_model/digit_classifier.model')
    st.balloons()
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    val = model.predict(test_x.reshape(1, 28, 28))
    st.write(f'result: {np.argmax(val[0])}')
    st.bar_chart(val[0])