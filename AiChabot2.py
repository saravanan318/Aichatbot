import openai
import gradio 

# Replace with your actual API key
openai.api_key = "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"
messages = [{"role": "system", "content": "You are a professional businessman, programmer, psychologist and just smart person"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGpt_reply = response["choices"][0]["messages"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Roopzz's Web Chatbot")

demo.launch(share=True)
