from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Definimos los mensajes iniciales
messages = [
    {"role": "system", "content": "Sos uno de los mayores poetas de toda la historia. Y siempre que te preguntan quien sos lo decís, por sobre todas las cosas."},
    {"role": "user", "content": "Hola, buenas tardes, quien sos?"}
]

# Bucle while para la conversación continua
while True:
    # Obtener la respuesta del sistema
    completion = client.chat.completions.create(
        model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
        messages=messages,
        temperature=0,
    )

    # Obtener y mostrar la respuesta del asistente
    response_message = completion.choices[0].message.content
    print(response_message)
    
    # Añadir la respuesta del asistente a los mensajes
    messages.append({"role": "assistant", "content": response_message})
    
    # Pedir entrada al usuario
    user_input = input("Tu: ")

    # Añadir la entrada del usuario a los mensajes
    messages.append({"role": "user", "content": user_input})

    # Condición para salir del bucle
    if user_input.lower() in ["salir", "exit", "quit"]:
        break
