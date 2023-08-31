import websockets
import asyncio
PORT = 5001
print(f"Started Server...Listening on port {PORT}")
async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            print(f"Received Message from client: {message}")
            await websocket.send("Response: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        print(e)

start_server = websockets.serve(echo,"143.110.254.115",PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()