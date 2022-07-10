Streamlit web app: Classify handwritten digist
=====

A lightweight and super fast C/C++ library for sequence alignment using [edit distance](https://en.wikipedia.org/wiki/Edit_distance).

Calculating edit distance of two strings is as simple as:
```c
edlibAlign("hello", 5, "world!", 6, edlibDefaultAlignConfig()).editDistance;
```

Edlib is also available for **Python** [![PyPI version](https://img.shields.io/pypi/v/edlib.svg) (Click here for Python README)](https://pypi.python.org/pypi/edlib), with code residing at [bindings/python](bindings/python).

Developers have created bindings to edlib in other languages as well:

* [Edlib.jl](https://github.com/cjdoris/Edlib.jl), a Julia package created and supported by Christopher Rowley ([@cjdoris](https://github.com/cjdoris))
* [edlibR](https://github.com/evanbiederstedt/edlibr), an R package created and supported by Evan Biederstedt ([@evanbiederstedt](https://github.com/evanbiederstedt))

## Get started

Please install python 3.8

Clone this repository and go into the project directory
```c
git clone https://github.com/thaisbendixen/streamlit_digit_classifier

cd streamlit_digit_classifier
```

Create a virtual environment or use the devcontainer.

Install requirements
```c
pip install -r requirements.txt
```

Run machine learning model
```c
python handwritten_number_classification/digit_classifier_model/digit_classifier_model.py 
```

Run streamlit app
```c
streamlit run handwritten_number_classification/streamlit_app.py
```