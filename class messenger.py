class Messenger:
    def __init__(self, username):
        self.username = username
        self.inbox = []
    def send_message(self, receiver, message):
        receiver.receive_message(self.username, message)
        print("Message sent successfully.")
    def receive_message(self, sender, message):
        self.inbox.append((sender, message))
    def read_messages(self):
        if not self.inbox:
            print("No new messages.")
        else:
            print(f"Messages for {self.username}:")
            for sender, message in self.inbox:
                print(f"From {sender}: {message}")
