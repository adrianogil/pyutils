from .clitools import run_cmd
import time
import sys

start_time = time.perf_counter()    # 1

output = run_cmd(cmd=sys.argv[1:], live_log=True)

end_time = time.perf_counter()      # 2
run_time = end_time - start_time    # 3
print(f"\n[Finished in {run_time:.4f} secs]")

python_module_not_found_exception = 'ModuleNotFoundError'
python_error_message = 'No module named '

if python_module_not_found_exception in output:
    print('\n\nParsing script output for errors')

    python_path = sys.argv[1]

    output_lines = output.split('\n')
    for line in output_lines:
        if python_module_not_found_exception in line:
            txt_index = line.index(python_error_message)
            module_name = line[txt_index + len(python_error_message) + 1:-1]
            module_name = module_name.strip()
            print("- Module not found: '%s' Would you like to install it? ([y]/N)" % (module_name,))
            answer = input()
            if answer == '\n' or answer.lower() == 'y':
                pip_install_cmd = python_path + ' -m pip install ' + module_name
                run_cmd(pip_install_cmd, live_log=True)
