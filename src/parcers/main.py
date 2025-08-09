import asyncio
import logging

parce_site_queue = asyncio.Queue()
parce_site_results_queue = asyncio.Queue()

logger = logging.getLogger(__name__)


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
    logger.info("Starting parce site workers")
    workers = [asyncio.create_task(parce_site_worker()) for _ in range(count_workers)]
    await asyncio.gather(*workers, return_exceptions=True)
