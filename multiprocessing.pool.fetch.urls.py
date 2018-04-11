import requests 
import threading 
from time import time
from pprint import pprint


def fetch_file(index, results): 
    print(F"Thread #{index + 1}")
    start = time()
    r = requests.get("http://speedtest.ftp.otenet.gr/files/test1Mb.db")
    results[index] = {
        'size': len(r.text), 
        'time': time() - start 
    }
    print(F"done #{index + 1}")
    
if __name__ == '__main__': 
    start = time()
    
    results = {}
    for i in range(20): 
        t = threading.Thread(target=fetch_file, args=(i, results))
        t.start()
        
    main_thread = threading.main_thread()
    
    for thread in threading.enumerate(): 
        if thread is main_thread: 
            continue 
            
        thread.join()
        
    
    
    print(F"All done {time() - start}(s)")
    pprint(results)
        
