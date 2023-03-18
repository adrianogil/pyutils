""" Module responsible for smart creation of dunder init files """
from pyutils.cli.clitools import run_cmd

import sys
import os


def generate_init(target_dir, include_to_git=True):
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    init_file = os.path.join(target_dir, '__init__.py')

    with open(init_file, 'w') as target_file_handler:
        target_file_handler.write('\"\"\" Init file \"\"\"\n')

    if include_to_git:
        run_cmd('git add "%s"' % (target_dir,))


if __name__ == '__main__':
    args = sys.argv[1:]

    include_to_git = True

    if '--no-git' in args:
        args.remove('--not-git')
        include_to_git = False

    if len(args) > 0:
        target_dir = args[0]
    else:
        target_dir = os.getcwd()

    generate_init(target_dir, include_to_git=include_to_git)

    # Walk through all subdirectories of the target directory
    for root, dirs, files in os.walk(target_dir):
        for directory in dirs:
            # Do something with the directory name
            sub_dir_path = os.path.join(root, directory)
            print("Add init to path: ", sub_dir_path)
            generate_init(sub_dir_path, include_to_git=include_to_git)
