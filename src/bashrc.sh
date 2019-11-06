
if [ -z "$PYTOOLS_PYTHON_PATH" ];
then
    export PYTOOLS_PYTHON_PATH=$PYTOOLS_DIR/python/
    export PYTHONPATH=$PYTOOLS_PYTHON_PATH:$PYTHONPATH
fi

alias py-pickle-viewer="python3 $PYTOOLS_DIR/python/pyutils/pickle_view.py"
alias py-json-load="python3 -i $PYTOOLS_DIR/python/pyutils/json_load.py"
