import requests 
from time import time
import multiprocessing 
from pprint import pprint


def fetch_file(index): 
    print(F"Thread #{index + 1}")
    start = time()
    r = requests.get("http://speedtest.ftp.otenet.gr/files/test1Mb.db")
    print(F"done #{index + 1}")
    return dict(size=len(r.text), time=time()-start), index
    
if __name__ == '__main__': 
    start = time()
    results  = {}
    with multiprocessing.Pool(4) as pool:
        threads = [
            pool.apply_async(fetch_file, (i,))
            for i in range(20)
        ]
        
        for t in threads: 
            result, index = t.get()
            results[index] = result
            
        

    
    print(F"All done {time() - start}(s)")
    pprint(results)
        
