import openai

openai.api_key = "sk-w8I67UjAP4Cvvb2yyA7g944Y4x9NgxPHS0PCkjBhOlT3BlbkFJKT4ZGRvRGS3KqFZ7yHRqL9K7wmkbRZFq34ARzcbvoA"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content']

def chat():
    print("Welcome to the classfit AI chat app! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    chat()