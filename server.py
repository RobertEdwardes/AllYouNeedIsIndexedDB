import asyncio
import websockets

connections = set()

async def hello(websocket):
    connections.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            websockets.broadcast(connections, message)
    finally:
        connections.remove(websocket)
    

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())