import vk_api
from rich.console import Console
from rich.progress import track

console = Console()

class ChangeProfile:
    """change of status"""
    def __init__(self, sessions):
        self.status_vk = console.input('[bold red]status vk> [/]')
        for session in track(sessions,
        '[bold white]CHANGE[/]'):
            self.status_set(session)

    def status_set(self, session):
        session = vk_api.VkApi(token=session)
        vk = session.get_api()

        try:
            vk.status.set(text=self.status_vk)

        except Exception as error:
            console.print(f'[bold red]ERROR[/]: {error}')
