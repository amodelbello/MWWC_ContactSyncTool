#!/bin/bash

if [ "$1" == "-d" ]; then
    PYTHONBREAKPOINT=remote_pdb.set_trace REMOTE_PDB_HOST=127.0.0.1 REMOTE_PDB_PORT=4000 python -m flask --app mwwc_sync_contacts run --debug
else
    python -m flask --app mwwc_sync_contacts run --debug
fi
