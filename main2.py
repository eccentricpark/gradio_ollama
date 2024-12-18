"""
============================================
Tulu3 8B
이전 답변을 기억하는 로직 작성
============================================
"""
import gradio
import ollama

model_name = "tulu3"
messageList = []

def ai_response(input):

    # 유저 입력 내용 추가
    messageList.append({
        'role' : "user",
        "content" : input
    })

    response = ollama.chat(
        model="tulu3", 
        messages=[{
            'role' : 'system',
            'content' : ''
        },
        *messageList
    ])
    
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
