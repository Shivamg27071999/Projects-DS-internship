from openai import OpenAI
import streamlit as st

f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("Shivam Generated AI")
st.subheader('ssooonnn')

# client.create_completion("Hello world")

prompt = st.text_input('Enter a data science topic')
if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"Generate 3 data Science questions and answer for MCQ test."},
            {"role":"user","content":prompt}
    ]
    )

    if response.choices:
        st.write(response.choices[0].message.content)
