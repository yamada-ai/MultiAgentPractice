from typing import List

from .base import BaseEnvironment
from multiagent.agents.base import BaseAgent
from multiagent.message import Message

class Environment(BaseEnvironment):
    def __init__(self,
            agents: List[BaseAgent],
            max_turns:int = 10,
            cnt_turn:int = 0,
            last_messages:List[Message]= [],
        ) -> None:
        super().__init__(agents, max_turns, cnt_turn, last_messages)
    
    async def step(self):
        pass

