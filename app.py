import streamlit as st
import pickle

# Load the trained model from a local file
model_path = 'Email_Spam_Detection/model.pkl'

try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: Model file not found. Please check the path.")
    model = None
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    model = None

# Create title
st.title('Predicting if a message is Spam or Not')

# Text input
message = st.text_input('Enter a message')

# Prediction button
submit = st.button('Predict')

if submit and model is not None:
    prediction = model.predict([message])

    if prediction[0] == 'spam':
        st.warning('This message is Spam')
    else:
        st.success('This message is Legit (Ham)')
        st.balloons()