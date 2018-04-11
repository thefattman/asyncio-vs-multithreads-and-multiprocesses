import requests 
from time import time
from pprint import pprint

def fetch_file(index): 
    start = time()
    print(F"Attempt {index + 1}")
    r = requests.get("http://speedtest.ftp.otenet.gr/files/test1Mb.db")    
    print(F"Done #{index + 1}")
    return len(r.text), time() - start
    
if __name__ == '__main__':
    start = time()
    results = {}
    for i in range(4): 
        file_size, time_taken = fetch_file(i)
        results[i] = {
            'size': file_size, 
            'time': time_taken
        }
        
    print(F"All done {time() - start}(s)")
    pprint(results)
    
