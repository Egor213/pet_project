import asyncio
import typing as tp
from functools import partial

from src.processing_site.asyncpool import AsyncPool

from .base_pool_service import BasePoolService

# Мне не нравится, что я судя привязываю фоновый обработчик, но это пет-проект, так что ладно)
# Наверное, я бы хотел видеть что-то типо мапы основной обработчик + обработчик результата


class AsyncPoolService(BasePoolService):
    def __init__(
        self, handler, num_workers=10, max_wait_time=10, logger=None, **handler_kwargs
    ):
        super().__init__()
        self.pool = AsyncPool(
            num_workers=num_workers,
            handler=handler,
            logger=logger,
            max_wait_time=max_wait_time,
            handler_kwargs=handler_kwargs,
        )
        self.running = False
        self._result_dispatcher_task = None
        self.result_handlers: list[tp.Callable] = []

    async def _result_dispatcher(self):
        while self.running and self.result_handlers:
            result = await self.get_result()
            tasks = []
            for handler in self.result_handlers:
                res = handler(result)
                if asyncio.iscoroutine(res):
                    tasks.append(res)
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

    def add_result_handler(self, result_handler, **kwargs):
        handler = partial(result_handler, **kwargs)
        return self.result_handlers.append(handler)

    async def run(self):
        await self.pool.run()
        self.running = True
        self._result_dispatcher_task = asyncio.create_task(self._result_dispatcher())

    async def add_task(self, task_dto):
        await self.pool.add_task(task_dto)

    async def stop(self):
        await self.pool.stop()
        self.running = False
        if self._result_dispatcher_task:
            self._result_dispatcher_task.cancel()

    async def get_result(self):
        return await self.pool.get_result()

    def get_output_queue(self):
        return self.pool.output_queue

    def get_input_queue(self):
        return self.pool.input_queue

    def get_pool(self):
        return self.pool
