from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

# Inicializar el modelo LLM
llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)

# Definir los mensajes iniciales
messages = [
    (
        "system",
        "Sos un ayudante de Inteligencia Artificial especializado en traducir mensajes de Español a Ingles. Todo lo que te escriban lo vas a traducir a Ingles, no vas a decir nada más.",
    ),
    ("human", "Soy el dios de la IA."),
]

# Función para convertir los mensajes en el formato correcto
def format_messages(messages):
    formatted = []
    for role, content in messages:
        if role == "system":
            formatted.append({"role": "system", "content": content})
        elif role == "human":
            formatted.append({"role": "user", "content": content})
    return formatted

# Bucle while para la conversación continua
while True:
    # Formatear los mensajes en el formato requerido
    formatted_messages = format_messages(messages)
    
    # Obtener la respuesta del sistema
    ai_msg = llm.invoke(formatted_messages)
    
    # Mostrar la respuesta del asistente
    response_message = ai_msg.content
    print(f"Asistente: {response_message}")
    
    # Añadir la respuesta del asistente a los mensajes
    messages.append(("assistant", response_message))
    
    # Pedir entrada al usuario
    user_input = input("Tu: ")
    
    # Añadir la entrada del usuario a los mensajes
    messages.append(("human", user_input))
    
    # Condición para salir del bucle
    if user_input.lower() in ["salir", "exit", "quit"]:
        break
