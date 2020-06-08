#!/bin/bash

WORKDIR="/home/peanut/dotz"

echo "Perfomando operações necessárias "

sudo /etc/init.d/mysql start

if [ $? -eq 0 ]; then
    echo "Database Não Iniciado"
else
    echo "Database não foi iniciado"
fi

export PYTHONPATH=:${PYTHONPATH}:${pwd}

pip install -r requirements.txt

python3 $WORKDIR/business/main.py >> relatorio_de_execução.txt

