# Współbieżność w Pythonie

## Synchronous Version

```
def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration_sync = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
```
## Threading Version
```
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration_thread = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
```

## Asyncio Version
```
async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    nest_asyncio.apply()
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration_asyncio = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
```
## Multiprocessing Version
```
session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration_multiproc = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
```
## CPU-Bound Synchronous Version
```
def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
```
## CPU-Bound Multiprocessing Version
```
def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
```
## Porównanie czasów
```
Synchronic: 3.0520334243774414 seconds
Threading: 1.0360848903656006 seconds
Asyncio: 3.0479607582092285 seconds
Multiprocessing: 2.229825496673584 seconds 
```
## Synchronous Script
```
def download_images():
    response = requests.get("https://picsum.photos/v2/list")
    if response.status_code != 200:
        raise AttributeError('GET /tasks/ {}'.format(response.status_code))
    data = json.loads(response.text)[:10]

    pictures=[]
    for s in data:
        pictures.append(s['download_url']+".jpg")
    return pictures

def saveImages(link):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    request.urlretrieve(link, "picture/{}.{}".format(filename, fileformat))

def main():
    images = download_images()
    for image in images:
        saveImages(image)

start_time = time.time()
main()
duration_synch = time.time() - start_time
print(f"Time taken: {duration_synch}")
```

## Multithreading
```
def process_images_threading():
    images = download_images()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(saveImages,images)

start_time = time.time()
process_images_threading()
duration_multithreading = time.time() - start_time
print(f"Time taken: {duration_multithreading}")
```
## Asyncio

```
async def download_images_asyncio(link, session):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    async with session.get(link) as response:
        with open("picture/{}.{}".format(filename, fileformat), 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)

async def main_asyncio():
    images = download_images()

    async with aiohttp.ClientSession() as session:
        tasks=[download_images_asyncio(image,session)for image in images]
        return await asyncio.gather(*tasks)

start_time = time.time()
nest_asyncio.apply()
asyncio.run(main_asyncio())
duration_asyncio = time.time() - start_time
print(f"Time taken: {duration_asyncio}")
```

## Porównanie czasów
```
Synchronous: 6.709909915924072
Multithreading: 1.7608542442321777
Asyncio: 1.3208708763122559
```
