import subprocess
import os


def run_cmd(cmd, terminal_executable=None, return_stderr=False, load_bashrc=False, live_log=False):
    ibash_exe = "/usr/local/bin/interactive_bash"

    if cmd:
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

    if not live_log:
        subprocess_output = subprocess.check_output(subprocess_cmd, **args)
        subprocess_output = subprocess_output.decode("ISO-8859-1")
        subprocess_output = subprocess_output.strip()
    else:
        subprocess_output = ''

        if cmd.__class__ == str:
            subprocess_cmd = subprocess_cmd.split(' ')

        process = subprocess.Popen(subprocess_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            output = None

            try:
                output = process.stdout.readline()
            except Exception as exception:
                output = None

            if output is None or (output == b'' and process.poll() is not None):
                break
            if output:
                out = output.decode("ISO-8859-1")
                subprocess_output += out + '\n'
                print(out, end="")

    return subprocess_output
