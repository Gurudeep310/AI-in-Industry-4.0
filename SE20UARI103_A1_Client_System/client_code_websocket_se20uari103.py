#Write a Program in python to send a message from client system to server system and vice versa.

#Use the library websocket.

import websockets
import asyncio

async def listen():
    url = "ws://143.110.254.115:5001"
    async with websockets.connect(url) as websocket:
        await websocket.send("Hello Server!")
        while True:
            message = await websocket.recv()
            print(message)

asyncio.get_event_loop().run_until_complete(listen())

