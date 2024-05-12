from .flags import process_args

class CliController:
    def get_commands(self):
        commands =  [

        ]

        return commands


class CliApp:
    def __init__(self, controller: CliController):
        self.controller = controller

    def run(self):
        args = process_args()
        self._parse_commands(args)

    def _parse_commands(self, args):
        if args is None:
            return

        commands_parse = self.controller.get_commands()

        # print('DEBUG: Parsing args: ' + str(args))
        for a in args:
            if a in commands_parse:
                if commands_parse[a](args[a], args, self.controller):
                    break
        else:
            print('Command not found')
