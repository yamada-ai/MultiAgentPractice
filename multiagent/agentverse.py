import asyncio
from typing import List

from multiagent.agents.base import BaseAgent
from multiagent.environments.base import BaseEnvironment
from multiagent.initialize import *


class AgentVerse:

    def __init__(
            self,
            agents: List[BaseAgent],
            environment: BaseEnvironment
        ) -> None:
        self.agents = agents
        self.environment = environment
    
    @classmethod
    def from_config(cls, conf_fname, config_path="./multiagent/"):
        
        config = load_config(conf_fname, config_path)
        agents_config = config["agents"]
        env_config = config["environment"]
        # print(agents_config)
        agents = []
        for ag_conf in agents_config:
            agents.append(build_agent(ag_conf))
        environment = build_environment(env_config, agents)
        return cls(agents, environment)

    def run(self):
        """Run the environment from scratch until it is done."""
        self.environment.reset()
        while not self.environment.is_done():
            asyncio.run(self.environment.step())

    def reset(self):
        self.environment.reset()
        for agent in self.agents:
            agent.reset()
    
    # このコードは正直意味不明
    def next(self, *args, **kwargs):
        return_message = asyncio.run(self.environment.step(*args, **kwargs))
        return return_message