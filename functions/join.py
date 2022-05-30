import vk_api
from rich.console import Console
from rich.progress import track
from rich.prompt import Prompt, Confirm
import time

from functions.function import FunctionSettings

console = Console()

class JoinChat(FunctionSettings):
    """join to chat"""
    def __init__(self, sessions):
        self.delay_flood(sessions)

        self.link = console.input('[bold red]link> ')
        self.delay = Prompt.ask('[bold red]delay[/]', default='0')

        for session in track(sessions,
        '[bold white]CHANGE[/]'):
            self.joined(session)

    def joined(self, session):
        session = vk_api.VkApi(token=session)
        vk = session.get_api()

        try:
            vk.messages.joinChatByInviteLink(link=self.link)

        except Exception as error:
            console.print(f'[bold red]ERROR[/]: {error}')

        time.sleep(int(self.delay))
