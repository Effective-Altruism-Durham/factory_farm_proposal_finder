import ollama

response = ollama.chat(model="gemma:2b-instruct-q4_0", messages=[{"role": "user", "content": "Tell me a joke."}])
print(response["message"])