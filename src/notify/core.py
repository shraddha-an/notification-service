"""Contains the base notification channel interface."""

class Notifier:
    def __init__(self, channel) -> None:
        self.channel = channel
    def send(self, message: str) -> None:
        self.channel.send(message)