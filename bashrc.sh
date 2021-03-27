alias p2='python2'
alias p3i='python3 -i'

function p3()
{
    python3_path=$(which python3)
    python3 -m pyutils.cli.runpythoncmd ${python3_path} $*
}

function p3m()
{
    if [[ -z "$1" ]]; then
        module_path=$(find . -name '*.py' | cut -c3- | default-fuzzy-finder)
    else
        module_path=$1
    fi
    module_path=${module_path%"/__init__.py"}
    target_module=$(echo ${module_path} | tr '/' '.')
    target_module=${target_module/.py/}
    echo "Running module "${target_module}
    shift
    p3 -m ${target_module} $@
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

alias pi-error="python3 -m pyutils.cli.get_pymodule_from_lasterror '$(history | tail -3 | head -1)'"
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
alias py-tg="python3 -m pyutils.pyproject.create_init_files"

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
