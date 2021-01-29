alias p2='python2'
alias p3='python3'

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
    python3 -m ${target_module} $@
}

function p3mi()
{
    module_path=$1
    target_module=$(echo ${module_path} | tr '/' '.')
    target_module=${target_module/.py/}
    echo "Running module "${target_module}
    shift
    python3 -i -m ${target_module} $@
}

alias pys="find . -name '*.py'"

alias pi-error="python3 -m pyutils.cli.get_pymodule_from_lasterror '$(history | tail -3 | head -1)'"
alias pi="pip install"

alias py-tree="tree -I *.pyc -I __pycache__"

# Create init files
alias py-tg="python3 -m pyproject.create_init_files"

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

if [ -z "$PYTOOLS_PYTHON_PATH" ];
then
    export PYTOOLS_PYTHON_PATH=$PYTOOLS_DIR/python/
    export PYTHONPATH=$PYTOOLS_PYTHON_PATH:$PYTHONPATH
fi

alias py-pickle-viewer="python3 $PYTOOLS_DIR/python/pyutils/pickle_view.py"
alias py-json-load="python3 -i $PYTOOLS_DIR/python/pyutils/json_load.py"
