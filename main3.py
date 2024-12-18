"""
============================================
Tulu3 8B
- 이전 답변을 기억하는 로직 작성
- json으로 작성된 시스템프롬프트를 적용용
============================================
"""
import gradio
import ollama
import json


model_name = "tulu3"
messageList = []

def getPromptByJson():
    with open('./prompt.json', 'r', encoding="utf-8") as file:
        file_data = json.load(file)
    return file_data

def ai_response(input):

    # 유저 입력 내용 추가
    messageList.append({
        'role' : "user",
        "content" : input
    })

    response = ollama.chat(
        model="tulu3", 
        messages=[getPromptByJson(), *messageList]
    )
    answer = response['message']['content']

    # 모델 답변 내용 추가, 이전 답변 내용을 기억하기 위한 용도
    messageList.append({
        'role' : "assistant",
        "content" : answer
    })
    return answer

def main():
    app = gradio.Interface(
        fn=ai_response, 
        inputs="text", 
        outputs="text",
        title="Tulu3 8B",
        description="Allen ai에서 만든 Tulu3 8B입니다.",

    )
    app.launch()

main()
