#!/bin/bash

WORKDIR="/home/peanut/dotz"

echo "Perfomando operações necessárias "

sudo /etc/init.d/mysql start

if [ $? -eq 0 ]; then
    echo "Database iniciado"
else
    echo "Database não foi iniciado"
    exit
fi

export PYTHONPATH=:${PYTHONPATH}:${pwd}

pip install -r requirements.txt

python3 $WORKDIR/business/main.py

echo ""

