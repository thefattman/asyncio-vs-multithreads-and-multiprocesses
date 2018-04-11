import requests 
from time import time
from pprint import pprint
import asyncio

async def fetch_file(index, results): 
    start = time()
    print(F"Attempt {index + 1}")
    task = loop.run_in_executor(None, requests.get, "http://speedtest.ftp.otenet.gr/files/test1Mb.db")    
    r = await(task)
    print(F"Done #{index + 1}")
    return dict(index=i, size=len(r.text), time=time() - start)
    
if __name__ == '__main__':
    start = time()
    loop = asyncio.get_event_loop()
    
    tasks = []
    results = {}
    for i in range(120): 
        task = asyncio.ensure_future(fetch_file(i, results))
        print("doing something")
        tasks.append(task)
        
    responses = asyncio.gather(*tasks)
    loop.run_until_complete(responses)
        
    print("All Done ", time() - start, " sec")
    pprint(list(responses.result()))
