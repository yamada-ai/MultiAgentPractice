import os
from typing import Dict, List


import yaml

# 特に環境に置く内容ってなくね？
# 一応議論ターンと
def build_environment():
    pass

# エージェントの設定
def build_agent():
    pass

# エージェント設定
def load_config(conf_fname, config_path="./multiagent/"):
    try:
        with open(config_path+conf_fname, "r") as f:
            config = yaml.safe_load(f)
        print("(init) success load agent confg")
        return config
    except Exception as e:
        print("(init) failure load agent config")