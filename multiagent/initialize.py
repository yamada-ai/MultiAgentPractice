import os
from typing import Dict, List

from multiagent.agents.agent import Agent
from multiagent.environments.environment import Environment
from multiagent.memory.history import History

import yaml

# 特に環境に置く内容ってなくね？
# 一応議論ターンと
def build_environment(env_config:dict, agents: List[Agent]):
    environment = Environment(
        agents=agents,
        max_turns=env_config["max_turns"]
    )
    return environment

# エージェントの設定
# ここは一旦具体的なクラスを指定する
def build_agent(agent_config:dict):
    # print(agent_config.keys())
    agent_config["memory"] = History()
    agent = Agent(
        name=agent_config["name"],
        role_desc=agent_config["role_description"],
        prompt_templete=agent_config["prompt_template"],
        memory=History(),
        max_retry=agent_config["max_retry"]
    )
    # print(agent)
    return agent

# エージェント設定
def load_config(conf_fname, config_path="./multiagent/"):
    try:
        with open(config_path+conf_fname, "r") as f:
            config = yaml.safe_load(f)
        print("(init) success load confg")
        return config
    except Exception as e:
        print("(init) failure load config")