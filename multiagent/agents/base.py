from abc import abstractclassmethod
from typing import Set, List, NamedTuple, Union

from multiagent.message import Message
from multiagent.memory.base import BaseMemory

class BaseAgent:
	def __init__(self,
			name: str,
			role_desc: str,
			prompt_templete: str,
			memory : BaseMemory,
			max_retry:int,
			receiver:Set[str] = set({"all"})
		) -> None:
		self.name = name
		self.role_desc = role_desc
		self.prompt_template = prompt_templete
		self.memory = memory
		self.max_retry = max_retry
		self.receiver = receiver
	
	@abstractclassmethod
	def step(self, env_desc: str="") -> Message:
		pass

	@abstractclassmethod
	def astep(self, env_desc: str="") -> Message:
		pass

	@abstractclassmethod
	def reset(self) -> None:
		pass

	@abstractclassmethod
	def add_message_to_memory(self, messages: List[Message]) -> Message:
		pass

	def get_receiver(self) -> Set[str]:
		return self.receiver
	
	def set_receiver(self, receiver: Union[Set[str], str]) -> None:
		if isinstance(receiver, str):
			self.receiver = set({receiver})
		elif isinstance(receiver, set):
			self.receiver = receiver
		else:
			raise ValueError(
				"(BaseAgent:set)receiverの型が不正"
			)

	def add_receiver(self, receiver: Union[Set[str], str]) -> None:
		if isinstance(receiver, str):
			self.receiver = set({receiver})
		elif isinstance(receiver, set):
			self.receiver = self.receiver.union(receiver)
		else:
			raise ValueError(
				"(BaseAgent:add)receiverの型が不正"
			)

	def add_receiver(self, receiver: Union[Set[str], str]) -> None:
		if isinstance(receiver, str):
			try:
				self.receiver.remove(receiver)
			except KeyError as e:
				print(f"receiver({receiver})ねえぞ")
		elif isinstance(receiver, set):
			self.receiver = self.receiver.union(receiver)
		else:
			raise ValueError(
				"(BaseAgent:remove)receiverの型が不正"
			)

	def __repr__(self):
		return (
            f"BaseAgent(name={self.name}, role_desc={self.role_desc}, "
            f"prompt_template={self.prompt_template}, memory={self.memory}, "
            f"max_retry={self.max_retry}, receiver={self.receiver})"
        )	
