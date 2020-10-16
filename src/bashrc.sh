alias p2='python2'
alias p3='python3'

function p3m()
{
    module_path=$1
    target_module=$(echo ${module_path} | tr '/' '.')
    target_module=${target_module/.py/}
    echo "Running module "${target_module}
    shift
    python3 -m ${target_module} $@
}


alias pi-error="python3 -m pyutils.cli.get_pymodule_from_lasterror '$(history | tail -3 | head -1)'"
alias pi="pip install"

alias pytree="tree -I *.pyc -I __pycache__"

if [ -z "$PYTOOLS_PYTHON_PATH" ];
then
    export PYTOOLS_PYTHON_PATH=$PYTOOLS_DIR/python/
    export PYTHONPATH=$PYTOOLS_PYTHON_PATH:$PYTHONPATH
fi

alias py-pickle-viewer="python3 $PYTOOLS_DIR/python/pyutils/pickle_view.py"
alias py-json-load="python3 -i $PYTOOLS_DIR/python/pyutils/json_load.py"
