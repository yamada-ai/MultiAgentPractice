from typing import List, Set

class Message:
    def __init__(
            self,
            content: str = "",
            sender: str = "",
            receiver: Set[str] = set("all")
        ) -> None:
        
        self.content = content
        self.sender = sender
        self.receiver = receiver
