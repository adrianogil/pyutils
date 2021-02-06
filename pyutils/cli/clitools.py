import subprocess
import os


def run_cmd(cmd, terminal_executable=None, return_stderr=False, load_bashrc=False):
    ibash_exe = "/usr/local/bin/interactive_bash"

    subprocess_cmd = cmd

    args = {"shell": True}

    if terminal_executable is not None:
        args["executable"] = terminal_executable
    elif load_bashrc:
        if os.path.exists(ibash_exe):
            args["executable"] = ibash_exe
    if return_stderr:
        args["stderr"] = subprocess.STDOUT
        args["universal_newlines"] = True
        args["timeout"] = 3

    subprocess_output = subprocess.check_output(subprocess_cmd, **args)
    subprocess_output = subprocess_output.decode("utf8")
    subprocess_output = subprocess_output.strip()

    return subprocess_output
