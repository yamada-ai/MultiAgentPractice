from abc import abstractmethod
from typing import Dict, List

from multiagent.message import Message

class BaseMemory:
	def __init__(self, messages: List[Message] = []) -> None:
		self.messages = messages

	@abstractmethod
	def add_message(self, messages: List[Message]) -> None:
		pass

	@abstractmethod
	def to_string(self)-> str:
		pass

	@abstractmethod
	def reset(self) -> None:
		pass