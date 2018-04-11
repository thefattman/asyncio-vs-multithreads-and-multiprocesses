import requests 
from time import time
from pprint import pprint
import asyncio
import aiohttp

async def main(): 
    start = time()
    async with aiohttp.ClientSession() as session: 
        tasks = []
        for i in range(120):             
            task = asyncio.ensure_future(fetch_file(session, i))
            tasks.append(task)
            
        responses = await asyncio.gather(*tasks)
            
    
    print(F"All done {time() - start} seconds")
    pprint(responses)
        
                

async def fetch_file(session, i): 
    async with session.get('http://speedtest.ftp.otenet.gr/files/test1Mb.db') as response:
        print(F'task {i+1} started')
        start = time()
        result = await response.read() 
        print(F'task {i+1} done')
        return dict(
            index=i, 
            size=len(result), 
            time=time()-start
        )
    
    
if __name__ == '__main__': 
    start = time()
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main())
    loop.run_until_complete(task)
    
    
