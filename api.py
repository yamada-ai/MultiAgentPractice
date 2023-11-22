import requests
import asyncio

api_url = "https://api.adviceslip.com/advice"

async def aget_api_response():
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, requests.get, api_url)
    return res.json()["slip"]["advice"]

def get_api_response():
    res = requests.get(url=api_url)
    return res.json()["slip"]["advice"]