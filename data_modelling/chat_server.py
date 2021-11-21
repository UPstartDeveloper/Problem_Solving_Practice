"""
Chat Server: 
Explain how you would design a chat server. 
In particular, provide details about the various 
    backend components, 
    classes, and 
    methods. 
    
What would be the hardest problems to solve?

1. Scope:
    Why:
        - Messages - consumemr - frends and family
                   - semi-frequent convers
                   - somewhat 
    What:
        - iOS app - backend architecture
    Where:
        - global
            - TODO: localizing across
    When:
        - 7-8 x a day - high traffic
    How: 
        - internet connection
        - peer2peer networking
        - each device has its own local copy of all messages
        - TODO: encrypt messages

2. Core Object:
    - User
    - Device
    - ChatSession
    - Message object        
                            
                        ChatSession --> User ----> Message
                                         |
                                         |
                                       Device

3. Components:

    on a single device

        UI layer ----- backend layer ------ data tier 
                       (networking)         (store all msgs)

4. Methods

    MVC
        Resource = Message, ChatSession
        
        1) ChatSessionCreate
        2) MessageCreate
        3) MessageRead
        4) ChatSessionList
        5) ChatSessionDelete

5.

chat-server-project/
        |
        |
        chat_server/
                |
                |
                |
                chat_server/
                    settings.py
                    wsgi.py
                    urls.py
                |
                |
                |
                messages/
                    models.py - ChatSession, Message
                    urls.py - routes 
                    views.py - controller functions
                    templates/ - HTML for the views
                    



        
    

"""
