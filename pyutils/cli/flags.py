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


def verify_flag(flag_name: str) -> bool:
    """
    Verify if a given flag exists in the flags dictionary.

    :param flag_name: The name of the flag to verify.
    :return: True if the flag exists, False otherwise.
    """
    if not flags:
        process_args()  # Assumes process_args() populates the 'flags' dictionary

    return flag_name in flags


def get_flag(flag_name: str, default_value=None, prompt_label: str = None):
    """
    Get the value of a flag from a dictionary, with an option to prompt for the value.

    :param flag_name: The name of the flag to retrieve.
    :param default_value: Default value if the flag is not found.
    :param prompt_label: Label for the prompt if the flag value needs to be inputted.
    :return: The value of the flag or the default value.
    """
    if not flags:
        process_args()  # Assumes process_args() populates 'flags'

    if flag_name in flags:
        flag_value = flags[flag_name]
    elif prompt_label:
        prompt = f"{prompt_label}: " if default_value is None else f"{prompt_label} (default: {default_value}): "
        flag_value = input(prompt) or default_value
        flags[flag_name] = flag_value
    else:
        flag_value = default_value

    if isinstance(flag_value, list) and len(flag_value) == 1:
        return flag_value[0]

    return flag_value
