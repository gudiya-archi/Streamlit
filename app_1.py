import streamlit as st
import pandas as pd 

st.title("DataFrame Example")
df = pd.DataFrame({
    'name':['shiv','wonder','nishant'],
    'age':[20,21,22],
    'marks':[50,60,70],
    'package':[10,12,14]

})
st.data_editor(df)



st.title("metrics Example")
st.metric("Revenue", 'Rs 3L', '-3%')

st.title("Json Example")
st.json({
    'name':['shiv','wonder','nishant'],
    'age':[20,21,22],
    'marks':[50,60,70],
    'package':[10,12,14]
})
