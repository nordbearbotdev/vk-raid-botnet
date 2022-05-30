from rich.prompt import Prompt, Confirm

class FunctionSettings:
    def delay_flood(self, sessions):
        accs = int(Prompt.ask(
            '[bold red]how many accounts to use? [/]',
            default = str(len(sessions))
        ))

        self.sessions = sessions[:accs]
