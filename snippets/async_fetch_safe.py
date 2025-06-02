# 🚫 Before:
import asyncio, aiohttp

TOTAL_REQUESTS = 1_000_000


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def main():
    urls = [f"https://api.site/{i}" for i in range(TOTAL_REQUESTS)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)  # 💥 OOM / rate-limit


asyncio.run(main())


# ✅ After
import asyncio, aiohttp

TOTAL_REQUESTS = 1_000_000
sem = asyncio.Semaphore(1000)


async def fetch(session, url):
    async with sem:
        try:
            async with session.get(url) as resp:
                return await resp.text()
        except aiohttp.ClientError:
            return None


async def main():
    urls = [f"https://api.site/{i}" for i in range(TOTAL_REQUESTS)]
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(urls), 10_000):
            chunk = urls[i : i + 10_000]
            tasks = [fetch(session, url) for url in chunk]
            await asyncio.gather(*tasks)


asyncio.run(main())

# 🧠 ➤ Avoid memory blowups & rate-limit bans. Use semaphores + chunking like a pro.
