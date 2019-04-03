
if [ -z "$PYTOOLS_PYTHON_PATH" ];
then
    export PYTOOLS_PYTHON_PATH=$PYTOOLS_DIR/src
    export PYTHONPATH=$PYTOOLS_PYTHON_PATH:$PYTHONPATH
fi

alias py-pickle-viewer="python3 $PYTOOLS_DIR/src/python/pickle_view.py"