import argparse
import asyncio
import yaml
from multiagent import agentverse

# parser = argparse.ArgumentParser()

from api import get_api_response, aget_api_response, aget_quote

def main():
    # res = get_api_response()
    res =  asyncio.run(aget_quote())
    print(res)

    agent_num = 3

    with open("./multiagent/hoge.yaml", "r") as f:
        config = yaml.safe_load(f)
    # print(config["agents"][0])
    # load config

if __name__ == "__main__":
    main()