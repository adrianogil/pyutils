from pyutils.utils.userinput import get_user_input

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

    return flags


def verify_flag(flag_name: str) -> bool:
    """
    Verify if a given flag exists in the flags dictionary.

    :param flag_name: The name of the flag to verify.
    :return: True if the flag exists, False otherwise.
    """
    if not flags:
        process_args()  # Assumes process_args() populates the 'flags' dictionary

    return flag_name in flags


def get_flag(flag_name, default_value=None, prompt_label: str = None):
    """
    Get the value of a flag from a dictionary, with an option to prompt for the value.

    :param flag_name: The name of the flag to retrieve.
    :param default_value: Default value if the flag is not found.
    :param prompt_label: Label for the prompt if the flag value needs to be inputted.
    :return: The value of the flag or the default value.
    """
    if not flags:
        process_args()  # Assumes process_args() populates 'flags'

    flag_value = None

    if flag_name.__class__ == list:
        flag_list = flag_name
        flag_name = flag_list[0]

        for f in flag_list:
            if f in flags:
                flag_name = f
                break
    if not flag_value and flag_name in flags:
        flag_value = flags[flag_name]
    elif prompt_label:
        prompt = f"{prompt_label}: " if default_value is None else f"{prompt_label} (default: {default_value}): "
        flag_value = get_user_input(prompt) or default_value
        flags[flag_name] = flag_value
    else:
        flag_value = default_value

    if isinstance(flag_value, list) and len(flag_value) == 1:
        return flag_value[0]

    return flag_value


def get_all_flags(exception_list=None, remove_dash=False):
    """
    Get all flags from the flags dictionary.
    """
    if not flags:
        process_args()  # Assumes process_args() populates 'flags'

    if exception_list:
        user_flags = {k: v for k, v in flags.items() if k not in exception_list}
    else:
        import copy
        user_flags = copy.deepcopy(flags)

    if remove_dash:
        user_flags = {k.replace("--", ""): v for k, v in user_flags.items()}

    return user_flags
