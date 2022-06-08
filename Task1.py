import asyncio
import aiohttp
import time

async def run(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(content)
            return content

async def main():
    obj1 = run("https://reqres.in/api/users?page1")
    obj2 = run("https://reqres.in/api/users?page2")
    obj3 = run("https://reqres.in/api/users?page3")

    # See that the three object would execute synchronously,
    # so it will take max(1, 2, 3) seconds to execute.
    start = time.time()

    await asyncio.gather(obj1, obj2, obj3)

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))

asyncio.run(main())
