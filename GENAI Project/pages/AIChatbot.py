from openai import OpenAI
import streamlit as st

f = open("keys\.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("Shivam Generated AI Chatbot")
st.subheader('ssooonnn')

# client.create_completion("Hello world")

prompt = st.text_input('Enter a topic')
if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a Education Counsellor working with a data science institute."},
        {"role": "user", "content": "Hello!"}
      ]
    )

    if response.choices:
        st.write(response.choices[0].message.content)
