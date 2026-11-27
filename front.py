import streamlit as st
import back

st.title("My Streamlit App")
st.write("Welcome to my Streamlit application! This is a simple " \
"example of how to use Streamlit to create interactive web applications with Python.")



def log ():
    back.log(dict(st.session_state))
    







cols = st.columns(4)

with cols[0]:
    st.chat_input("Ask me anything!", key="text1", on_submit=log)

with cols[1]:
    st.chat_input("Ask me anything!", key="text2", on_submit=log)


#st.write("state", st.session_state)

but1 = st.button("button")
# Initialization
if 'but1Pressed' not in st.session_state:
    st.session_state['but1Pressed'] = 0


#perserve button pressed as session variable
if but1:
    st.session_state['but1Pressed'] +=1


#pressed button logic
if st.session_state['but1Pressed']:
    with cols[2]:
        in1 = st.chat_input("new box1", key="text3", on_submit=log)
    with cols[3]:
        st.chat_input("new box2", key="text4", on_submit=log)

#FORM
with st.form("my_form"):
    checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("Submit")
    if submitted:
        print("submitted")