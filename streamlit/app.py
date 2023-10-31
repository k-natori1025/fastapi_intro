import streamlit as st
import pandas as pd
import numpy as np

st.title('Sample App')

st.markdown("""
# 見出し1
## 見出し2
            
- 箇条書き1
- 箇条書き2
""")

st.code("""
import numppy as np
import pandas as pd
a = 123
pd.DataFrame()
""")

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [-1, -2, -3, -4]
})

st.dataframe(df.style.highlight_max(axis=0))

st.json({
    'data':{
        'name': 'abc',
        'age': 123
    }
})

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

if st.button('Click Me!'):
  st.write('Clicked')

if st.checkbox('Click Me!'):
  st.write('Clicked')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write(f'You selected: {options}')

number = st.sidebar.slider('Pick a Num', 0, 100, 40)
st.sidebar.write(f'number: {number}')

left_col, center_col, right_col = st.columns(3)
left_col.slider('Pick a Num in Left', 0, 100, 40)
center_col.write('Center Column')
right_col.write('Right Column')


