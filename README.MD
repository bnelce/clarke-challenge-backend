Entra no conteiner do web:
sudo docker-compose exec web /bin/bash

executa as migrations:
flask db upgrade

Caso queira mexer no codigo (fora do conteiner web):
1 - entra na .venv: source .venv/bin/activate
2 - instala as dep: pip install -r requirements.txt

rodar localmente:

python3 -m venv venv
source venv/bin/activate

windows:
venv\Scripts\Activate.ps1

rodar apenas o banco de dados (sem o conteiner do web):
sudo docker-compose up --scale web=0
