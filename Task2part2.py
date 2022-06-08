import asyncio
import time
import urllib.request
import aiohttp
import aiofiles
import json
import ast

async def download_pep(pep_number):
    print(pep_number)
    async with aiohttp.ClientSession() as session:
         async with session.get("https://xkcd.com/%d/info.0.json"%pep_number) as resp:
            content = await resp.read()
            #print(content)
    name=('asynciosxkcd%d.json'%pep_number)
    dict_str = content.decode("UTF-8")
    data = ast.literal_eval(dict_str)
    json_string = json.dumps(data)
    with open(name, 'w') as outfile:
        outfile.write(json_string)
    print("The json file %d written"%pep_number)
    return content
    
async def main():
    tasks = []
    for i in range(1,201):
        tasks.append(download_pep(i))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")
