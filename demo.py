import streamlit as st
import numpy as np
import pandas as pd
import time


st.title('demo')

st.code('''def foo(x)
    x = x**3 + x**5
    return x**2''',language='python')   # code block to be run in the streamlit console and output the result to the streamlit page.'')


data = pd.read_csv('electricity.csv')


st.write(data.head(50))




chart = st.line_chart(data.iloc[:,[1,2,3]])

# for i in range(data.shape[0]):
#     chart.add_rows(data.iloc[i,1])
#     time.sleep(0.05)