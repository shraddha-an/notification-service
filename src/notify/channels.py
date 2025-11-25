"""Contains interfaces for notification channels."""

from notify.schema import Message

# mock Email Channel implementation
class ConsoleEmailClientAdapter:
    """A mock email client adapter that simulates sending emails by printing to the console."""
    def __init__(self, from_addr, to_addr):
        self.from_addr = from_addr
        self.to_addr = to_addr

    def send(self, message: Message) -> None:
        print(f"From: {self.from_addr}") 
        print(f"To: {self.to_addr}")
        print(f"\n")
        print(f"Subject: {message.subject}")
        print(f"\n")
        print(f"Body: {message.body}")
