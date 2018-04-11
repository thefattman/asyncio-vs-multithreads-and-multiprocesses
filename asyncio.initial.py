import requests 
from time import time
from pprint import pprint
import asyncio
import aiohttp

async def fetch_file(index, results): 
    start = time()
    print(F'Task #{index + 1} started')
    async with aiohttp.ClientSession() as session: 
        async with session.get('http://speedtest.ftp.otenet.gr/files/test1Mb.db') as response:
            result = await response.read() 
            results[index] = dict(size=len(result), time=time()-start)
            print(F'Task #{index + 1} done')
        
    
    
    
if __name__ == '__main__': 
    start = time()
    results = {}
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(20): 
        task = asyncio.ensure_future(fetch_file(i, results))
        tasks.append(task)
        
    loop.run_until_complete(asyncio.wait(tasks))
    print(F"All done {time() - start} seconds")

    
