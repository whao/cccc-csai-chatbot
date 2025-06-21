# 导入必要的库
from openai import OpenAI
import streamlit as st
import os

# 设置 Streamlit 应用的标题
st.title("ChatGPT-like clone")

# 使用环境变量中的 API 密钥初始化 OpenAI 客户端
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# 检查会话状态中是否设置了 OpenAI 模型，如果没有，则设置默认模型
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# 如果会话状态中没有消息列表，则初始化为空列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示会话状态中存储的所有历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 处理用户在聊天输入框中的输入
if prompt := st.chat_input("What is up?"):
    # 将用户的消息添加到会话状态中
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 在聊天界面中显示用户的消息
    with st.chat_message("user"):
        st.markdown(prompt)

    # 使用 OpenAI API 生成助手的回复
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # 在聊天界面中显示助手的回复
        response = st.write_stream(stream)
    
    # 将助手的回复添加到会话状态中
    st.session_state.messages.append({"role": "assistant", "content": response})