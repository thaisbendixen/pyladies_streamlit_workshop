# write text with st.write()
import streamlit as st

st.write("This is my first web app! YAY")



# write text with st.table()
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 15),
    columns=(f"this is column {i}" for i in range(15)))
st.table(dataframe)

## solution
# write text with st.table() and st.line_chart()
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 15),
    columns=(f"this is column {i}" for i in range(15)))

st.table(dataframe)
st.line_chart(dataframe)
# only first 5 columns
st.line_chart(dataframe.iloc[:,:5])



# write text with st.selectbox()
import streamlit as st

option = st.selectbox(
    'How has the workshop been going so far?',
     ["", "great", "\U0001f600", "just ok"])

'You selected: ', option

## solution
# write text with st.selectbox() and st.sidebar...()
import streamlit as st

option = st.sidebar.selectbox(
    'How has the workshop been going so far?',
     ["", "great", "\U0001f600", "just ok"])

'You selected: ', option



# write text with st.selectbox() and st.columns....()
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 15),
    columns=(f"this is column {i}" for i in range(15)))

st.table(dataframe)
st.line_chart(dataframe)
# only first 5 columns
st.line_chart(dataframe.iloc[:,:5])

## solution
# write text with `st.selectbox()` and `st.columns....()`:
import streamlit as st

left_column, right_column = st.columns(2)

option = left_column.selectbox(
    'How has the workshop been going so far?',
     ["", "great", "\U0001f600", "just ok"])

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    st.write(f"You selected: {option}")
