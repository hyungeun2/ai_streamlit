import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('킹받는 넝~담봇😜')

st.image("https://t1.daumcdn.net/news/202302/03/BoiledMovie/20230203190929191lbmx.png", width = 400)

keyword = st.text_input("키워드를 입력하세요")

if st.button('생성하기'):
    with st.spinner('넝~담 제조중...'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyword,
                },
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 킹받는 농담 하나만 작성해줘.",
                }
            ],
            model="gpt-4o",
        )

    result = chat_completion.choices[0].message.content
    st.write(result)