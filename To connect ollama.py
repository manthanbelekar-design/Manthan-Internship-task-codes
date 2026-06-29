import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Search for Manthan Belekar on Google"}
    ]
)

print(response["message"]["content"])