# Tráfego Rodoviário API

Este projeto desenvolve uma API REST utilizando Django Rest Framework para alimentar uma dashboard de monitoramento de tráfego rodoviário. A API fornece informações detalhadas sobre segmentos de estrada, incluindo a velocidade dos veículos, a caracterização da intensidade do tráfego e a localização.

## Tabela de Conteúdos

1. [Documentação da API](#documentação-da-api)
2. [Documentação do Repositório](#documentação-do-repositório)
3. [Instruções de Configuração e Utilização](#instruções-de-configuração-e-utilização)
4. [Testes](#testes)

## Documentação da API

### Endpoints

A API possui os seguintes endpoints principais, gerenciados através de um `ModelViewSet`:

- **Segmentos de Estrada**
  - `/traffic/roadsegments/`: Lista todos os segmentos de estrada.
  - `/admin/`: Inicia sessão de administrador para editar, adicionar, eliminar dados.
  - `/api/docs/`: Documentação interativa da API (swager).


### Permissões de dos utilizadores

Os tipos de utilizadores e suas permissões são:

- **Administrador**
  - Pode criar, ler, atualizar e eliminar segmentos de estrada.

- **Anónimo**
  - Pode apenas ler segmentos de estrada.

### Caracterização da Intensidade do Tráfego

A intensidade do tráfego é inferida a partir da velocidade média dos veículos e classificada conforme a tabela abaixo:

| Velocidade Média | Intensidade |
|------------------|-------------|
| ≤ 20 km/h        | Elevada     |
| > 20 e ≤ 50 km/h | Média       |
| > 50 km/h        | Baixa       |

Os intervalos de velocidade podem ser ajustados no futuro, e a API deve refletir sempre as regras mais recentes.

## Documentação do Repositório

### Estrutura do Repositório

- `traffic/`: Aplicação Django para segmentos de estrada e leituras de velocidade.
  - `models.py`: Modelos Django para segmentos de estrada.
  - `serializers.py`: Serializadores para os modelos.
  - `views.py`: Lógica das views da API.
  - `urls.py`: URLs específicas da aplicação.

- `traffic_indicator/`: Diretório principal do projeto Django.
  - `settings.py`: Configurações do projeto.
  - `urls.py`: Configurações de URL do projeto, incluindo integração com Swagger.

- `README.md`: Este documento.

### Requisitos

- Django
- Django Rest Framework
- drf-yasg (para documentação Swagger)
- PostgreSQL

## Instruções de Configuração e Utilização

git clone https://github.com/jpprodrigues99/Exercicio_Ubiwhere.git



### Configuração da Base de Dados

A API utiliza PostgreSQL como base de dados. A configuração para o base de dados está definida em `settings.py` do projeto Django como segue:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_base_dados',
        'USER': 'nome_utilizadores',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': '5432',
    }
}
```
### Configurar ambiente django

- crie um ambiente virtual
- "source env/bin/activate" - (mac) para ativar o ambiente virtual
- "cd traffic_indicador" - Entre no reposiótio 
- "python manage.py migrate" - Execute as migrações para configurar a base de dados
- "python manage.py createsuperuser" - Crie um super utilizador para aceder ao Django Admin
- "python manage.py runserver" - Execute o servidor de desenvolvimento do Django

## Testes

Abaixo estão os testes unitários implementados para a aplicação. Estes testes garantem que a funcionalidade da API está funcionando conforme o esperado e que os dados dos segmentos de estrada estão sendo processados corretamente.

- Testes Unitários
Os testes estão localizados em traffic/tests.py e cobrem os seguintes aspectos:

- Intensidade do Tráfego
Verifica se a intensidade do tráfego é calculada corretamente com base na velocidade.
- Valores Padrão
Verifica se os valores padrão são definidos corretamente ao criar um novo segmento de estrada.
