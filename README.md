
## asyncio-vs-multithreads-and-multiprocesses

A small premier on the implementations of Multi threading and multi processing the normal way vs asyncio. 

This requires `asyncio` so you'll need python3 for the asyncio examples. All examples downloads a 1MB file using various techniques. This is to experiment with multithreading, multiprocessing and `asyncio`. 


```
# Downloading 1MB using requests and sequential downloads
$ python simple.fetch.py
```
```
# Downloading 1MB using `threading` module
$ python threading.fetch.urls.py
```
```
# Downloading 1MB using `multiprocessing` module
$ python multiprocessing.pool.fetch.urls.py
```
```
# Downloading 1MB using `asyncio` - simply modifying the simple.fetch.py code
$ python asyncio.simple.fetch.urls.py
```
```
# Downloading 1MB using `asyncio` - using aiohttp client - better way of doing simply.fetch.py
$ python asyncio.initial.py
```
```
# Downloading 1MB using `asyncio` - using aiohttp client - more optimized approach
$ python asyncio.optimized.py
```


