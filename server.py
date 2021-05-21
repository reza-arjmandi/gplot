import asyncio
import websockets
import json
import math
import time

class DataProvider:
    x = 0.0

    def provide(self, data_size):
        data = []
        data.append(['Time', 'Level', 'Level2'])
        for y in range(int(data_size)):
            data.append([self.x, math.sin(self.x), math.cos(self.x)])
            self.x = self.x + 1

        return json.dumps(
            {"data": data })

async def serve_req(websocket, path):
    while True:
        data_size = await websocket.recv()
        data = _provider.provide(data_size)
        await websocket.send(data)

_provider = DataProvider()
start_server = websockets.serve(serve_req, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
