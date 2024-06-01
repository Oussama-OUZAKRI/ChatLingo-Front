import asyncio
import websockets
import json

clients = set()

async def register(websocket):
    clients.add(websocket)
    print(f"Client connected: {websocket.remote_address}")

async def unregister(websocket):
    clients.remove(websocket)
    print(f"Client disconnected: {websocket.remote_address}")

async def handle_message(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"Received message: {data}")
            await broadcast(data)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {websocket.remote_address} - {e}")
    finally:
        await unregister(websocket)

async def broadcast(message):
    if clients:
        await asyncio.wait([client.send(json.dumps(message)) for client in clients])
        print(f"Broadcasted message: {message}")

async def main():
    print("Starting WebSocket server on ws://localhost:8765")
    async with websockets.serve(handle_message, "localhost", 8765):
        await asyncio.Future()  # Run forever

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Server stopped manually.")
