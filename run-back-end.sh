#!/bin/bash

source backend/env/bin/activate
cd backend 2>/dev/null
FLASK_APP=project/server.py python -m flask run --host=0.0.0.0
inactivate 2> /dev/null