#!/bin/bash

if [ "$1" == "-d" ]; then
    PYTHONBREAKPOINT=remote_pdb.set_trace REMOTE_PDB_HOST=127.0.0.1 REMOTE_PDB_PORT=4000 python -m flask --app run --debug
else
    python -m flask --app src run --debug
fi
