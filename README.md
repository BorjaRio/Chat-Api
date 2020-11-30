# Chat-Api

EL objetivo del proyecto es poder crear una Api y insertarla en una base de datos.

Asimismo , vamos a hacerle request a la api para poder extraer información.

Vamos a crear la API a través de Flask donde conectaremos la base de datos con los endpoints.

los endpoints son los siguientes:

    (GET) /chat/create
        Purpose: Create a conversation to load messages
        -Params: An array of users ids [user_id]
        -Returns: chat_id

    (GET) /chat/adduser
        -Purpose: Add a user to a chat, this is optional just in case you want to add more users to a chat after it's creation.
        -Params: chat_id, user_id
        -Returns: chat_id

    (GET or POST) /chat/addmessage
        -Purpose: Add a message to the conversation. Help: Before adding the chat message to the database, check that the incoming user is part of this chat id. If not, raise an exception.
        -Params:
        -chat_id: Chat to store message
        -user_id: the user that writes the message
        -text: Message text
        -Returns: message_id

    (GET) /chat/list
        -Purpose: Get all messages from chat_id
        -Returns: json array with all messages from this -chat_id
    (GET) /chat/sentiment
        -Purpose: Analyze messages from chat_id. Use NLTK sentiment analysis package for this task
        -Returns: json with all sentiments from messages in the chat


La base de datos elegida es MongoDB Compass:

Creamos las siguientes collections en MongoCompassDB:

    -user
    -chat
    -message

insertarmos 3 usuarios en Mongo: Pablo, Borja y Luis

insertamos el mensaje con el texto: victoria

insertamos los chats: player , campeonato (2 user_id) y resultado