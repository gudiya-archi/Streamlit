import streamlit as st

st.title("My Streamlit App")
st.title(" Startup Dashboard")

st.header("I am learning Streamlit")
st.subheader("This is a subheader")

st.write("This is a noramal text in Streamlit. You can use this to display information, instructions, or any other content you want to share with your users.")
st.write("Welcome to my Streamlit application! This is a simple  app to demonstrate the capabilities of Streamlit.")

st.markdown("""
### My favorite movies
- Race 3 
- Humshakals 
- Housefull                                    
  """   )

st.code("""
def foo (input):
    return foo**2

x =fo(2)    
 """)

st.latex('x^2 + y^2 + 2 = 0')


