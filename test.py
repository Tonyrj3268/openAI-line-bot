import openai
class chatgpt:
    def __init__(self):
        openai.organization = "org-tHt70UMGlNYxmVgdarPogPhh"
        openai.api_key = "sk-IM7S7Wzgs9ZCyBS6QsCoT3BlbkFJ5HQrrt0X6PIDBgjA3ZM"

    def translate(self,prompt):
        prompt = "請幫我翻譯以下文本成中文 " + prompt
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5
        )
        
        text = response.choices[0].text
        return text