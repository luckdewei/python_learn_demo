import asyncio
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


class TaskManager:
    """任务管理器"""

    def __init__(self):
        self.tasks = set()

    async def worker(self, name, duration):
        """工作协程"""
        logging.info(f"任务 {name} 开始")
        try:
            await asyncio.sleep(duration)
            logging.info(f"任务 {name} 完成")
            return f"{name}_result"
        except asyncio.CancelledError:
            logging.info(f"任务 {name} 被取消")
            raise

    async def create_tasks(self, count):
        """创建多个任务"""
        for i in range(count):
            task = asyncio.create_task(
                self.worker(f"worker_{i}", i + 1), name=f"task_{i}"
            )
            self.tasks.add(task)
            task.add_done_callback(self.tasks.discard)

        logging.info(f"创建了 {count} 个任务")

    async def monitor_tasks(self):
        """监控任务状态"""
        while True:
            running_tasks = [t for t in self.tasks if not t.done()]
            logging.info(f"运行中的任务: {len(running_tasks)}")

            if not running_tasks:
                break

            await asyncio.sleep(0.5)

    async def cancel_all_tasks(self):
        """取消所有任务"""
        logging.info("取消所有任务")
        for task in self.tasks:
            task.cancel()

        await asyncio.gather(*self.tasks, return_exceptions=True)


async def task_management():
    """任务管理演示"""
    manager = TaskManager()

    await manager.create_tasks(5)
    monitor_task = asyncio.create_task(manager.monitor_tasks())

    await asyncio.sleep(2)
    await manager.cancel_all_tasks()

    await monitor_task


asyncio.run(task_management())
