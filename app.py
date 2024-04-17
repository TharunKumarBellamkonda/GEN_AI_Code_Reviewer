import streamlit as st
from openai import OpenAI

## Setting up OpenAI and key
with open('keys/.openai_api_key.txt') as f:
    OPENAI_KEY = f.read().strip()
client = OpenAI(api_key=OPENAI_KEY)
st.snow()

### title for the app
st.header(":rainbow[An AI]")
st.subheader(":rainbow[Python Code Reviewer]")
### Defining User and System Prompt
user_prompt = st.text_area(":orange[Please Enter your python code here] 🥲")
system_prompt = '''
    You are an intelligent Python code reviewer.
    You must verify the code and if it is incorrect, show the errors to the user and provide the correct code.
'''

### Generating response on button click
if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    st.write(response.choices[0].message.content)

    # Add a thank you note
    st.write(":red[Thank you for using the Python Code Reviewer!]")
