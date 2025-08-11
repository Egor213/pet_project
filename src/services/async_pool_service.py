from src.processing_site.asyncpool import AsyncPool


class AsyncPoolService:
    def __init__(self, handler, num_workers=10, logger=None):
        self.pool = AsyncPool(
            num_workers=num_workers,
            handler=handler,
            logger=logger,
        )

    async def run(self):
        await self.pool.run()

    async def add_task(self, task_dto):
        await self.pool.add_task(task_dto)

    async def stop(self):
        await self.pool.stop()

    async def get_result(self):
        return await self.pool.get_result()

    async def get_output_queue(self):
        return self.pool.output_queue

    async def get_input_queue(self):
        return self.pool.input_queue

    async def get_pool(self):
        return self.pool
