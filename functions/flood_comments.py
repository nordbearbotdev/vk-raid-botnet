from rich.progress import track
import vk_api
from rich.console import Console
from rich.prompt import Prompt, Confirm
from multiprocessing import Process
import random
import time

from functions.function import FunctionSettings
from settings.config import *

console = Console()

class CommentsFlood(FunctionSettings):
    """flood to comments"""
    def __init__(self, sessions):
        self.delay_flood(sessions)

        self.link_post = console.input('[bold red]list to the post: [/]').split('/')[3][4:].split('_')
        msg_connents_type = Confirm.ask('[bold red]take a message in the config?[/]')

        if msg_connents_type:
            self.message = text
        else:
            self.message = [console.input('[bold red]message> [/]')]

        self.delay = Prompt.ask("[bold red]delay[/]", default="1")

        console.print(self.link_post[0], self.link_post[1])

        processes = []

        for session in (self.sessions):

            process = Process(
                target=self.comments, args=(session,)
                )
            process.start()
            processes.append(process)

        for process in processes:
            process.join()

    def comments(self, session):
        session = vk_api.VkApi(token=session)
        vk = session.get_api()
        user = vk.users.get()

        count = 0
        count_error = 0

        for _ in range(count_range):
            try:
                vk.wall.createComment(
                owner_id=self.link_post[0],
                post_id=self.link_post[1],
                message=random.choice(self.message)
                )
                count += 1
                console.print(f'<{user[0]["first_name"]}> [bold green]sent[/] COUNT: [{count}]')

            except Exception as error:
                count_error += 1
                console.print(f'[bold red]not sent[/] {error}')

            if count_error == 3:
                break

            time.sleep(int(self.delay))
