from string import Template
from typing import List

from multiagent.message import Message

from .base import BaseAgent

class Agent(BaseAgent):
    def __init__(self) -> None:
        pass

    def step(self, env_desc: str=""):
        pass

    def astep(self, env_desc: str=""):
        pass

    def add_message_to_memory(self, messages: List[Message]) -> None:
        self.memory.add_message(messages)

    def reset(self) -> None:
        self.memory.reset()