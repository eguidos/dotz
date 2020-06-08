# Ingestão de dados 

## Table of contents

1. Resumo
2. Solução
    - Proposta modelo relacional - MER
    - Nomalização dos dados utilizando Python Pandas
3. Resultados

* Resumo

O conteúdo deste repositório tem como objetivo demonstrar um fluxo e dados para realizar a ingestão de dados utiliando o fremework **Pandas**. Além disso, um relatório contendo os dados obtidos pelo processo
de ingestão será diponibilizado no diretório base do projeto.

* Solução

Como destacado anteriormente, o case foi solucionado como base a tecnologia **Pandas**.

* Proposta de modelo relacional

O modelo relacional foi implementado sob o banco relacional MySql 5.7 conforme o

![MER](model/mer.jpeg?raw=true "Title") 

Logicamente, o modelo foi segmentado em três principais components para a xtração de Entidade e Relacionamento.

1. Tabelas Dimensionais:
    - Price
    - Components
2. Tabela Fato
    - Bill
3. [Mysql](https://www.mysql.com/) 
4. [Pandas](https://pandas.pydata.org/)

### Normalização de dados utilizando Python

![DATA](normalization.jpeg?raw=true)

A organização do código Python utilizada projeto seguiu o padrão semelhante a Arquitetura Orientada a Serviços (SOA) evidenciado abaixo. Este padrão contribui para fácil manutenção do código fonte e principalmente para escalabilidade de análises sob o dado coletado.

#### DAO (Database Access Object)
Este componente tem como principal responsabilidade padronizar por meio de uma interface o acesso a diversos conjuntos de dados(inicialmente csv's).

#### Commom
Este componente tem como principal responsabilidade manter pequenos trechos de códigos que são comumnente utilizados pelas stack's de regra de negócio

#### Model
Este componente tem como principal responsabilidade manter um dicionário de dados para cada tabela final gerada na stack das regras de negócio.

#### Business
Este componente tem como principal responsabilidade implementar as regras de negócio.


***Para realizar a execução no Google Cloud GCP siga os passos a seguir*** 
 
- No Linux/Ubuntu:

1. Copie a chave de acesso que está no díretório.

     Abra o terminal (CTRL+ALT+t)
    `cp key/keys.pub /home/{seu_uruario}/.ssh`
    - Solicite a inicialização da instância no Google Coud ao [OWNER](https://github.com/eguidos) do projeto.

2. Conecte ao servidor via `ssh peanut@{ip_fornecido}

3. Acesse o diretório /dotz contido na WorkMachine:
    `cd dotz/`
4. Execute o arquivo `run.sh` para instalação das dependências necessárias para execução do pipeline de ingestão.
    `./run.sh`
    
- Windows via Putty:

O Putty é um software de código livre, que tem como objetivo simular um terminal SSH para o Windows. Através deve é possível manter conexões SSH, Telnet e até tuneis.
1. Abra o PuTTY. Caso não tenha, realize o download acessando o site [Putty.org](htts://putty.org)

2. À esquerda, na configuração, em Connection->SSH->Auth temos o campo “Private key file for authentication”. Clique em Browse e carregue o arquivo com sua chave privada:

3. - Solicite a inicialização da instância no Google Coud ao [OWNER](https://github.com/eguidos) do projeto.

4. Agora volte no item Session para informar os dados de conexão e salvar a sessão.

5. Em Host Name, preencha com o nome do servidor de acesso `peanut`.

6. Em Port, informe a porta 22 (padrão do SSH).

7. Mantenha SSH, que é o protocolo de comunicação.

8. Em Saved Session (marcado com verde), informe um nome para essa sessão.

9. Clique no botão Sasve para salvar a sessão, assim você não precisará ficar informando o arquivo de chave privada toda vez que for conectar.

10. Selecione a sua sessão salva e clique no botão Open.

11. Repita os pasos 3 e 4 descritos na execução em sistemas `Linux/Ubuntu`

#### Resultados
    
O relatório contendo as execuções serão apresentados dada a execução do arquivo `run.sh`
Os dados gerados após a execução do processo serão armazenados nas tabelas Bill, Price e Components.

Para vizualizar os dados inseridos siga os passos abaixo:

- Digite `mysql -u root -p` em seguida `admin` para password;

- Digite os comamndos:

    `use industry;` 
    
    `select * from bill;`
    
    `select * from components;`
    
    `select * from components;`

