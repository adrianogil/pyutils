import sys


flags = {

}

def get_parsed_flags():
    '''
        return parsed flags as a dictionary
    '''
    import pyutils.utils.datautils as datautils
    args = {}

    last_key = ''

    for i in range(1, len(sys.argv)):
        a = sys.argv[i]
        if a[0] == '-' and not datautils.is_float(a):
            last_key = a
            args[a] = []
        elif last_key != '':
            arg_values = args[last_key]
            arg_values.append(a)
            args[last_key] = arg_values

    return args


def process_args(flags_list=None):
    '''
        process current flags
        adds to internal storing system
    '''
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


def get_flag(flag_name, default_value=None, prompt_label=None):
    flag_value = default_value

    if not list(flags.keys()):
        process_args()

    if flag_name in flags:
        flag_value = flags[flag_name]
    elif prompt_label:
        if default_value:
            flags[flag_name] = input(f"{prompt_label} (default: {default_value}):")
        else:
            flags[flag_name] = input(f"{prompt_label}:")
        flag_value = flags[flag_name]

    if flag_value.__class__ == list and len(flag_value) == 1:
        flag_value = flag_value[0]

    return flag_value
