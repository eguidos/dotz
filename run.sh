#!/bin/bash

WORKDIR="/home/peanut/dotz"

echo "Perfomando operações necessárias "

python3 -m pip install -r requirements.txt

sudo /etc/init.d/mysql start

if [ $? -eq 0 ]; then
    echo "Database iniciado"
else
    echo "Database não foi iniciado"
    exit
fi

export PYTHONPATH=:${PYTHONPATH}:${pwd}



python3 $WORKDIR/business/main.py

if [ $? -eq 0 ]; then
    echo "Data Pipline concluido"
else
    echo "Houveram erros durante a execução do Pipline"
    exit
fi

