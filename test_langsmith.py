import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 自动读取 .env 里的 LANGCHAIN_TRACING_V2 和 API_KEY
load_dotenv()

# 初始化 DeepSeek 模型
llm = ChatOpenAI(
    model="deepseek-chat", 
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
    base_url="https://api.deepseek.com"
)

print("正在发送测试请求到 DeepSeek...")
response = llm.invoke("1+1等于几？请用一句话回答。")
print("收到回复:", response.content)
print("✅ 如果没有报错，数据已经暗中发送给 LangSmith 了！")