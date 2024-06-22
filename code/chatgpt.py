import g4f

class ChatGpt:
    def __init__(self) -> None:
        self.chat_history = []


    def send_message(self, message: str) -> str:
        user_message = {
            "role": "user", 
            "content": message
        }

        self.chat_history.append(user_message)    

        response = ""

        while True:
            try:
                response: str = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.chat_history)
                break     
            except:
                continue    
        
        
        assistant_message = {
            "role": "assistant",
            "content": response
        }

        self.chat_history.append(assistant_message)

        return response
        

    def reset_chat_history(self) -> None:
         self.chat_history = []