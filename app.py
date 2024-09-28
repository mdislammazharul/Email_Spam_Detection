import streamlit as st # type: ignore
import pickle

# loading the trained model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Predicting if message is Spam or not')

# text input
message = st.text_input('Enter a message')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])

    if prediction[0] == 'spam':
        st.warning('This message is Spam')
    else:
        st.success('This message is Legit (Ham)')
        st.balloons()