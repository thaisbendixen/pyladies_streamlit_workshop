This workshop is (stream)LIT! 🔥
=====

This repository was created to accompany a Pyladies workshop. This repository serves
as a playground to learn how to use Streamlit to build web apps. Please find the complementary
[presentation here](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

## Requirements

- Python 3.8
- Virtual environment manager, example [venv](https://docs.python.org/3/library/venv.html#creating-virtual-environments), or [devcontainer](https://code.visualstudio.com/docs/remote/containers) plugin for VS Code
- Github account and github [CLI](https://cli.github.com/manual/installation)


## ⚡️ Get started

Open a terminal window and clone this repository:
```bash
git clone git@github.com:thaisbendixen/pyladies_streamlit_workshop.git

cd pyladies_streamlit_workshop
```

Create a virtual environment or use the devcontainer. Pleas ask mentors at the workshop if you need help.

Next install requirements:
```bash
pip install -r requirements.txt
```

# 🤸‍♀️ Streamlit playground

First we start by exploring the streamlit capabilities, by building a few small web apps. To create your 
app please use [my_first_app.py](https://github.com/thaisbendixen/pyladies_streamlit_workshop/tree/main/my_first_app.py).

To build your first app add the following lines to the file mentioned above:
```
import streamlit as st

st.write("This is my first web app! YAY")
```

To start and run your app in the terminal write:
```bash
streamlit run streamlit_playground/my_first_app.py
```

The above command will open a window in your browser with your web app. You can edit the 
[my_first_app.py](https://github.com/thaisbendixen/pyladies_streamlit_workshop/blob/main/my_first_app.py)
file and rerun your app on the browser to see your most current changes.

# 🤖 Digit classification app

After you have explored streamlit for this workshop we prepared a machine learning project 
that classifies handwritten digits in a web app. See example here. We provide the solution here. If you are new
to machine learning we recommend looking at the [google colab file](https://github.com/thaisbendixen/pyladies_streamlit_workshop/blob/main/handwritten_number_classification/digit_classifier_model/Handwiritten_digit_classification_model.ipynb).

To create and train machine learning model run:
```bash
python handwritten_number_classification/digit_classifier_model/digit_classifier_model.py 
```

Run streamlit app:
```bash
streamlit run handwritten_number_classification/digit_classification_app.py
```

# Resources

A lot of this code is recycled from the following resources and was combined to create this workshop:

-

