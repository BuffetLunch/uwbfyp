import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect()
    await drone.action.arm()
    await drone.action.takeoff()

    async def print_position(drone):
        async for position in drone.telemetry.position_velocity_ned():
            print(position)

    asyncio.ensure_future(print_position(drone))

if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
