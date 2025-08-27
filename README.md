APP de Revenda de Carros



# Django Master - Carros Revenda

Este é um projeto Django para cadastro, listagem, edição e exclusão de carros, com autenticação de usuários e integração com a API da OpenAI, monitoramento com logger, criado para Gerenciamento e Revenda de carros relíquia.

## Funcionalidades

- Cadastro de usuários e autenticação (login/logout)
- Cadastro, listagem, edição e exclusão de carros
- Upload de fotos dos veículos
- Geração automática de bio/descritivo do carro via OpenAI
- Controle de inventário de carros e valor total

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repo.git
   cd DjangoMaster
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure o banco de dados e variáveis de ambiente no arquivo `.env`.

5. Aplique as migrações:
   ```sh
   python manage.py migrate
   ```

6. Crie um superusuário (opcional):
   ```sh
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Uso

- Acesse `http://localhost:8000/cars/` para listar os carros.
- Faça login ou registre-se para cadastrar, editar ou remover carros.
- O campo "bio" do carro é preenchido automaticamente usando a OpenAI.

## Estrutura do Projeto

- `cars/` - App principal de carros
- `accounts/` - App de autenticação de usuários
- `core/` - Configurações do projeto
- `openai_api/` - Integração com a API da OpenAI

## Licença

Este projeto é apenas para fins educacionais e de demonstração. Não é destinado a uso em produção.


