import ollama

response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': 'Teach me about Bitcoin',
    }
])

print(response['message']['content'])
