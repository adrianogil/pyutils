from .clitools import run_cmd

import subprocess
import sys

last_command = " ".join(sys.argv[1].strip().split(" ")[1:])
last_command = last_command.strip()

try:
    run_cmd(last_command, terminal_executable="/usr/local/bin/interactive_bash", return_stderr=True)
except Exception as error:
    get_error = str(error)

print("error")
print(get_error)
