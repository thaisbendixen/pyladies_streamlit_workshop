This workshop is (stream)LIT! 🔥
=====

This repository was created to accompany a [Pyladies](https://berlin.pyladies.com/) workshop. It serves
as a playground to learn how to use [streamlit](https://streamlit.io/) to build web apps. 
Please find the complementary [presentation here](https://docs.google.com/presentation/d/1yj1qCiDyQunhgzqnaa_cXDTogXCBYdUy_nRmmxwdr9A/edit#slide=id.g13b08c34cdd_0_6).

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

To add functionalities to your streamlit app please refer to the [streamlit documentation](https://docs.streamlit.io/).

# Resources

A lot of this code is recycled from the following resources and was combined to create this workshop:

- [Streamlit theme showcasing](https://github.com/streamlit/theming-showcase)
- [End-to-End Handwritten digits detection project using Streamlit](https://medium.com/@puspakmeher3/end-to-end-handwritten-digits-detection-project-using-streamlit-1e81b906f524)
- [Sketched Number Prediction App Using Streamlit](https://medium.com/datev-techblog/sketched-number-prediction-app-using-streamlit-43760861e6d5)
- [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk&t=1007s)
- [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk&t=1007s)
