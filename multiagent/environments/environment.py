from typing import List

class Environment:
    def __init__(self,
            agents,
            max_turns:int = 10,
            cnt_turn:int = 0,
            last_messages:List[str]= [],
        ) -> None:
        self.agents = agents
        self.max_turns = max_turns
        self.cnt_turn = cnt_turn
    
    async def step(self):
        pass

