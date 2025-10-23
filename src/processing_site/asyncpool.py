import asyncio
import logging
import typing as tp
from dataclasses import dataclass, field


class Terminator:
    pass


@dataclass
class AsyncPool:
    num_workers: int
    handler: tp.Callable
    logger: logging.Logger = field(default_factory=logging.getLogger)
    workers: list[asyncio.Task] = field(default_factory=list, init=False)
    max_wait_time: int = field(default=10)
    input_queue: asyncio.Queue = field(default_factory=asyncio.Queue, init=False)
    output_queue: asyncio.Queue = field(default_factory=asyncio.Queue, init=False)

    def __post_init__(self):
        self.input_queue = asyncio.Queue()
        self.output_queue = asyncio.Queue()

    async def worker_loop(self):
        while True:
            try:
                task_dto = await self.input_queue.get()
                if isinstance(task_dto, Terminator):
                    break
                result = await asyncio.wait_for(self.handler(task_dto), timeout=self.max_wait_time)
                await self.output_queue.put(result)
            except (KeyboardInterrupt, SystemExit) as e:
                self.logger.info(f"Worker received exit signal: {e}")
                break
            except Exception as e:
                self.logger.exception(f"Worker call failed: {e}")
                await self.output_queue.put(e)
            finally:
                self.input_queue.task_done()

    async def run(self):
        self.workers = [asyncio.create_task(self.worker_loop()) for _ in range(self.num_workers)]


    async def add_task(self, task_dto):
        await self.input_queue.put(task_dto)

    async def get_result(self):
        return await self.output_queue.get()

    async def stop(self):
        for _ in range(self.num_workers):
            await self.input_queue.put(Terminator())
        await self.input_queue.join()
        await asyncio.gather(*self.workers, return_exceptions=True)

    async def __aenter__(self):
        if not self.workers:
            await self.run()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()


@dataclass
class ParceSiteDto:
    url_site: str


async def worker(task_dto: ParceSiteDto):
    print(task_dto.url_site)
    await asyncio.sleep(3)
    print("Done")
    return task_dto.url_site


async def main():
    async with AsyncPool(num_workers=3, handler=worker) as pool:
        for i in range(6):
            task_dto = ParceSiteDto(f"https://google.com_{i}")
            await pool.add_task(task_dto)

        results = [await pool.get_result() for _ in range(6)]
        print(results)


if __name__ == "__main__":
    asyncio.run(main())
