import sys


flags = {

}


def process_args(flags_list=None):
    if flags_list is None:
        flags_list = sys.argv[1:]

    current_flag = ""
    current_values = []

    def add_flag(flag, value):
        if flag != "":
            flags[flag] = value

    for f in flags_list:
        if f.startswith('-'):
            add_flag(current_flag, current_values)
            current_flag = f
            current_values = []
        else:
            current_values.append(f)
    add_flag(current_flag, current_values)


def verify_flag(flag_name):
    if not list(flags.keys()):
        process_args()

    return flag_name in flags

def get_flag(flag_name):

    if flag_name in flags:
        return flags[flag_name]

    return None
