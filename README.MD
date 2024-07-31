# Projeto de Fornecedores de Energia

## Objetivo do Repositório

Este projeto foi desenvolvido como parte de um desafio técnico para a posição de Desenvolvedor Fullstack na Clarke Energia. O objetivo é criar uma aplicação web que permita aos usuários consultar fornecedores de energia elétrica com base no consumo mensal informado. O sistema deve retornar uma lista de fornecedores que podem atender à necessidade do usuário, juntamente com informações detalhadas sobre cada fornecedor.

## Requisitos do Projeto

1. **Entrada de Dados:** O usuário deve informar seu consumo mensal de energia (em kWh).
2. **Listagem de Fornecedores:** Com base no consumo informado, o sistema deve listar os fornecedores que podem atender ao cliente, considerando o limite mínimo de kWh de cada fornecedor.
3. **Informações do Fornecedor:** Para cada fornecedor, o sistema deve exibir as seguintes informações:
   - Nome
   - Logo
   - Estado de origem
   - Custo por kWh
   - Limite mínimo de kWh
   - Número total de clientes
   - Avaliação média dos clientes

## Tecnologias Utilizadas

- **Arquitetura:**

  - Clean Architecture (para manter a separação de responsabilidades e modularidade)

- **Backend:**

  - Python
  - Flask
  - SQLAlchemy
  - Ariadne (GraphQL)
  - PostgreSQL
  - Flask-Migrate (Migrações)

- **Frontend:**

  - A ser integrado (exemplo de stack sugerida: React, Vite, Apollo Client)

- **Infraestrutura e Testes:**
  - Docker
  - Docker Compose
  - pytest (para testes)

## Manual de Utilização

### Pré-requisitos

1. Docker
2. Docker Compose

### Instalação e Configuração

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/projeto-fornecedores-energia.git
   cd projeto-fornecedores-energia
   ```

2. **Configuração do Banco de Dados:**

- O banco de dados PostgreSQL será iniciado automaticamente pelo Docker Compose usando as configurações definidas no `docker-compose.yml`.

3. **Iniciar o Projeto com Docker Compose**

```bash
docker-compose up
```

- Isso irá iniciar os serviços definidos no docker-compose.yml, incluindo o aplicativo web e o banco de dados PostgreSQL.

4. **Inicializar o Banco de Dados e Realizar Migrações:**

   - Após os containers estarem em execução, abra um novo terminal e execute:

   ```bash
   docker-compose exec web flask db upgrade
   ```

   - Isso aplicará as migrações ao banco de dados.

5. **Executar os Testes:**

   - Para executar os testes, use o seguinte comando:

   ```bash
   docker-compose exec web pytest
   ```

   Isso executará todos os testes localizados no diretório tests.

6. **Acessar a aplicação:**

A aplicação estará disponível em http://localhost:5000/.
