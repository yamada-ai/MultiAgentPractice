from abc import abstractmethod
from typing import List

from multiagent.agents.base import BaseAgent
from multiagent.message import Message

class BaseEnvironment:
    def __init__(self,
            agents: List[BaseAgent],
            max_turns:int = 10,
            cnt_turn:int = 0,
            last_messages:List[Message]= [],
        ) -> None:
        self.agents = agents
        self.max_turns = max_turns
        self.cnt_turn = cnt_turn
        self.last_messages = last_messages

    @abstractmethod    
    async def step(self) -> List[Message]:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    def is_done(self) -> bool:
        return self.cnt_turn >= self.max_turns
