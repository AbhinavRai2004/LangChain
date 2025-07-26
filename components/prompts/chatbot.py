from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

chat_history = [
    SystemMessage(content='You are a helpful AI assistant'),
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break

    output = model.invoke(chat_history)

    chat_history.append(AIMessage(content=output.content))

    print(f"Bot: {output.content}")

print("Chat History: ",chat_history)