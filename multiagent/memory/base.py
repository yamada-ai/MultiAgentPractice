from abc import abstractclassmethod
from typing import Dict, List

from multiagent.message import Message

class BaseMemory:
	@abstractclassmethod
	def add_message(self, messages: List[Message]) -> None:
		pass

	@abstractclassmethod
	def to_string(self)-> str:
		pass

	@abstractclassmethod
	def reset(self) -> None:
		pass