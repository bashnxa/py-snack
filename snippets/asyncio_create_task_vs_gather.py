# 🚫 Before:
import asyncio
async def main():
    await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(2),
    )
asyncio.run(main())


# ✅ After
import asyncio
async def main():
    tasks = [
        asyncio.create_task(asyncio.sleep(1)),
        asyncio.create_task(asyncio.sleep(2)),
    ]
    await asyncio.gather(*tasks)
asyncio.run(main())

# 🧠 ➤ create_task() starts coroutines immediately, gives control — you can cancel, log, or await later. Perfect when spawn and await are in different places.
