alias p2='python2'
alias p3='python3'
alias p3i='python3 -i'
alias piu='pip install --upgrade pip'

function p3c()
{
    python3_path=$(which python3)
    python3 -m pyutils.cli.runpythoncmd ${python3_path} $*
}

function p3m()
{
    if [[ -d "$1" ]]; then
        module_path=$(find $1 -name '*.py' | cut -c3- | default-fuzzy-finder)
        pargs=${@:2}
    elif [[ -z "$1" ]]; then
        module_path=$(find . -name '*.py' | cut -c3- | default-fuzzy-finder)
        pargs=$@
    else
        module_path=$1
        if [ -f "$module_path" ]; then
            module_path=$1
        else 
            module_path=$(find . -name '*.py' | cut -c3- | default-fuzzy-finder)
        fi
        pargs=${@:2}
    fi
    module_path=${module_path%"/__init__.py"}
    target_module=$(echo ${module_path} | tr '/' '.')
    target_module=${target_module/.py/}
    echo "Running module "${target_module}
    p3 -m ${target_module} ${pargs}
}

function p3m()
{
    # Check if the first argument is a directory or a Python file
    if [[ -d "$1" ]]; then
        # If it's a directory, search for a Python file and prompt the user to select one
        module_path=$(find $1 -name '*.py' | default-fuzzy-finder)
        pargs=${@:2}
    elif [[ -z "$1" ]]; then
        # If no argument is specified, search for a Python file in the current directory and prompt the user to select one
        module_path=$(find . -name '*.py' | cut -c3- | default-fuzzy-finder)
        pargs=$@
    else
        # If a Python file is specified, use that as the module path
        module_path=$1
        if [ -f "$module_path" ]; then
            # Check if the specified file exists and is a file (not a directory)
            module_path=$1
        else 
            # If the specified file doesn't exist or is a directory, search for a Python file in the current directory and prompt the user to select one
            module_path=$(find . -name '*.py' | cut -c3- | default-fuzzy-finder)
        fi
        pargs=${@:2}
    fi
    
    # Remove the '/__init__.py' suffix (if present) and replace all slashes with dots to create the target module name
    module_path=${module_path%"/__init__.py"}
    module_path=${module_path%"/__main__.py"}
    target_module=$(echo ${module_path} | tr '/' '.')
    target_module=${target_module/.py/}
    
    # Print a message indicating which module is being run
    echo "Running module "${target_module}
    
    # Execute the Python module using the 'p3' command
    p3 -m ${target_module} ${pargs}
}


function p3mi()
{
    if [[ -z "$1" ]]; then
        module_path=$(find . -name '*.py' | cut -c3- | default-fuzzy-finder)
    else
        module_path=$1
    fi
    target_module=$(echo ${module_path} | tr '/' '.')
    target_module=${target_module/.py/}
    echo "Running module "${target_module}
    shift
    python3 -i -m ${target_module} $@
}

alias pys="find . -name '*.py'"

# alias pi-error="python3 -m pyutils.cli.get_pymodule_from_lasterror '$(history | tail -3 | head -1)'"
alias pi="pip install"

function pip-uninstall()
{
    target_module=$(pip freeze | grep '==' | tr '=' ' ' | default-fuzzy-finder | awk '{print $1}')

    echo "Uninstalling module "${target_module}
    pip uninstall ${target_module}
}
alias pu='pip-uninstall'

alias py-tree="tree -I *.pyc -I __pycache__"

# Create init files
function py-tg()
{
    echo "Running py-tg on current directory"
    python3 -m pyutils.pyproject.create_init_files
}

function py-smod()
{
    # Open module in sublime
    target_module=$1

    sublime -n $(python -c "import ${target_module} as o;import os; print(os.path.dirname(os.path.abspath(o.__file__)))")
}

function py-which()
{
    type python
}

alias py-pickle-viewer="python3 -i -m pyutils.pickle_view"
alias py-json-load="python3 -i -m pyutils.json_load"

function py-install-pyutils()
{
    pip install -e ${PYTOOLS_DIR}
}

function py-diff-days()
{
    target_day=$1
    python -m pyutils.cli.diffdays ${target_day}
}


function pydev-install-python()
{
    target_python=$(pyenv install --list | tail -n +3 | default-fuzzy-finder)
    pyenv install ${target_python##*( )}
}

function pydev-create-venv()
{
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt
}

function perfexe()
{
    python3 -m pyutils.cli.runperfcmd $1
}