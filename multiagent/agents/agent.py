from string import Template
from typing import List, Set

from multiagent.message import Message
from multiagent.memory.base import BaseMemory

from .base import BaseAgent

class Agent(BaseAgent):
    def __init__(self,
			name: str,
			prompt_templete: str,
			memory : BaseMemory,
			max_retry:int,
			receiver:Set[str] = set({"all"})
        ) -> None:
        super().__init__(name, prompt_templete, memory, max_retry, receiver)

    def step(self, env_desc: str=""):
        pass

    def astep(self, env_desc: str=""):
        pass

    def add_message_to_memory(self, messages: List[Message]) -> None:
        self.memory.add_message(messages)

    def reset(self) -> None:
        self.memory.reset()