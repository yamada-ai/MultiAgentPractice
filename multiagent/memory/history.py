from abc import abstractmethod
from typing import Dict, List

from multiagent.message import Message
from .base import BaseMemory

class History(BaseMemory):
	
    def __init__(self, messages) -> None:
        self.messages = messages
              
    def add_message(self, messages: List[Message]) -> None:
        for message in messages:
            self.messages.append(message)
    
    def to_string(self)-> str:
        pass
    
    def reset(self) -> None:
        self.messages = []