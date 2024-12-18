"""
============================================
Tulu3 8B
이전 답변을 기억하고 스트리밍 답변을 제공
============================================
"""
import gradio as gr
import ollama

model_name = "tulu3"
messageList = []

def ai_response(input):
    # 사용자 입력을 대화 기록에 추가
    messageList.append({
        'role' : "user",
        "content" : input
    })

    # 시스템 메시지와 대화 기록을 포함한 메시지 목록 생성
    response = ollama.chat(
        model="tulu3", 
        messages=[{
            'role' : 'system',
            'content' : '당신은 8년차 백앤드 개발자입니다. 코드를 제공할 때는 FastAPI + Layered Architecture 기반으로 제공하세요.'
        },*messageList], 
        stream=True
    )
    answer = ""

    # 스트리밍 응답 생성
    for chunk in response:
        answer += chunk['message']['content']
        yield answer

    # 모델의 최종 응답을 대화 기록에 추가
    messageList.append({'role': 'assistant', 'content': answer})

def main():
    # Gradio 입력항목 설정정
    app = gr.Interface(
        fn=ai_response,
        inputs="text",
        outputs="text",
        title="Tulu3 8B",
        description="Allen ai에서 만든 Tulu3 8B입니다.",
        analytics_enabled=True
    )
    app.launch()

if __name__ == "__main__":
    main()
