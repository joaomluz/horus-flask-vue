#!/bin/bash

if [ ! -f "INSTALL.path" ]; then
    echo "Run install-dependencies first"
    exit 1
fi

INSTALL_DIR=$(<INSTALL.path)
rm -f INSTALL.path 2> /dev/null

echo "Copying files ..."

cp -R ./* "${INSTALL_DIR}/" 2> /dev/null
chmod +x "${INSTALL_DIR}/run-back-end.sh"

cd "$INSTALL_DIR"

echo ""
echo "Configuring Python"
python3 -m venv backend/env
source "${INSTALL_DIR}/backend/env/bin/activate"
pip install Flask==1.1.2 Flask-Cors==3.0.10 pytest==6.1.1 Flask-SQLAlchemy==2.5.1
echo "[DB] Build"
python3 "${INSTALL_DIR}/backend/create_db.py"
inactivate 2> /dev/null
chmod +x run-back-end.sh

echo ""
echo "Configuring Vue"
npm install -g @vue/cli
vue --version
vue create client
npm install vue-router --save
npm install axios@0.21.1 --save
npm install bootstrap@4.6.0 --save