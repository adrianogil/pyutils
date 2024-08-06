
user_input_data = {

}

from prompt_toolkit import PromptSession

prompt_session = PromptSession()

def get_user_input(user_prompt, options=None, default_value=None):
    if default_value:
        user_prompt += f" ({default_value})"
    user_input = prompt_session.prompt(user_prompt)
    if not user_input:
        if options:
            from fzf_wrapper import prompt
            user_choice = prompt(options)
            if user_choice:
                user_input = user_choice[0]
                print(f"> {user_input}")
            else:
                user_input = default_value
        elif default_value:
            user_input = default_value
    return user_input
