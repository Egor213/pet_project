import asyncio

parce_site_queue = asyncio.Queue()
parce_site_results_queue = asyncio.Queue()


async def parce_site(url):
    await asyncio.sleep(1)
    return f"Processed {url}"


async def parce_site_worker():
    while True:
        try:
            url = await parce_site_queue.get()
            result = await parce_site(url)
            await parce_site_results_queue.put(result)
            print(f"Result: {result}")
            parce_site_queue.task_done()
        except asyncio.CancelledError:
            print("Worker cancelled")
            break


async def init_parce_site_workers(count_workers=10):
    workers = [asyncio.create_task(parce_site_worker()) for _ in range(count_workers)]
    urls = ["https://example.com", "https://yandex.ru", "https://google.com"]
    for url in urls:
        await parce_site_queue.put(url)
    await parce_site_queue.join()
    await asyncio.gather(*workers, return_exceptions=True)


# if __name__ == "__main__":
#     asyncio.run(init_parce_site_workers())
