import os

from dotenv import load_dotenv
import rootutils

ROOT_DIR = rootutils.setup_root(__file__, indicator='.project-root', pythonpath=True)
load_dotenv(ROOT_DIR / '.env')

from groq import Groq


client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# chat_completion = client.chat.completions.create(
#     messages=[
#         {'role': 'user', 'content': 'Explain the importance of fast language models'}
#     ],
#     model='llama3-70b-8192',
#     temperature=0
# )
# print(chat_completion.choices[0].message.content)

class Agent:
    def __init__(self, client: Groq, system: str = '') -> None:
        self.client = client
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({'role': 'system', 'content': self.system})

    def __call__(self, message: str = ''):
        if message:
            self.messages.append({'role': 'user', 'content': message})
        result = self.execute()
        self.messages.append({'role': 'system', 'content': result})
        return result

    def execute(self):
        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model='llama3-70b-8192',
            temperature=0
        )
        response = chat_completion.choices[0].message.content
        return response


if __name__ == '__main__':
    pass
