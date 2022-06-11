import vk_api
from rich.console import Console

console = Console()

class StatusAccount:
    """checking status account"""
    def __init__(self, sessions):
        count = 0
        error_count = 0

        for session in sessions:
            try:
                session = vk_api.VkApi(token=session)
                vk = session.get_api()

                user = vk.users.get()


                console.print(f'[bold green][+][bold white]{user[0]["first_name"]} id:[/]{user[0]["id"]}[/]')
                count += 1

            except Exception as error:
                console.print(f'[bold red][-][/]{error}')
                error_count += 1

        console.print(f'[bold]block: {error_count} normal: {count}[/]')
