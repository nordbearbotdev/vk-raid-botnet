from vkbottle.user import User, Message
from rich.prompt import Prompt, Confirm
from multiprocessing import Process
from rich.console import Console
import asyncio
import random

from functions.function import FunctionSettings
from settings.config import *

console = Console()

class Flood(FunctionSettings):
    """flood to chat"""
    def __init__(self, sessions):
        self.sessions = sessions

        self.delay_flood(self.sessions)
        self.delay = Prompt.ask("[bold red]delay[/]", default="1")

        self.started_flood()

    def flood(self, app, num_accs):
        self.session = User(app)

        #позже исправлю
        @self.session.on.message(text=trigger)
        async def flood_text(message: Message):
            user = await self.session.api.users.get()
            count = 0
            count_error = 0
            for _ in range(count_range):
                try:
                    await message.answer(random.choice(text))
                    count += 1
                    console.print(f'<{user[0].first_name}> [bold green]sent[/] COUNT: [{count}]')

                except Exception as error:
                    count_error += 1
                    console.print(f'[bold red]not sent[/] {error}')

                if count_error == 3:
                    break

                await asyncio.sleep(int(self.delay))

        self.session.run_forever()

    def started_flood(self):
        processes = []

        for num_accs, session in enumerate(
            self.sessions,
            start=1):

            process = Process(
                target=self.flood, args=(session, num_accs,)
                )
            process.start()
            processes.append(process)

        console.print(f'[*][bold white]SEND "[yellow]{trigger}[/]" to chat[/]')

        for process in processes:
            process.join()
