chmod +x install-*
sudo ./install-dependencies.sh /path/to/install/dir

FLASK_APP=project/server.py python -m flask run --host=0.0.0.0