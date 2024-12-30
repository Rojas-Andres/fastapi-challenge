# Challange by Andres Rojas

## correr proyecto

### Setup

1. Clone repository:

- `git clone https://github.com/Rojas-Andres/fastapi-challenge`
- `cd fastapi-challenge`

2. Copy `.env.example` to `.env` and custom:

- `cp .env.example .env`

### Correr proyecto con docker (recordar crear el .env en la raiz)
- ` docker-compose build `
- ` docker-compose up `

## Github CICD validaciones

#### Total de test ejecutados
![](images/github_actions/test_success.png)

#### Validacion de pre commit
![](images/github_actions/github_action_pre_commit_and_coverge_pass.png)

## Documentacion swagger
![](images/docs/swagger_doc.png)

## Diagrama ER
![](images/diagrama/diagrama_er.png)

## Despliegue AWS

#### Creacion params store en secrets manager para el template de cloudformation
![](images/deployment/creation_params_store.png)


#### Bucket para guardar las envs
![](images/deployment/bucket_save_envs.png)

#### Creacion de ECR para guardar imagenes de docker
![](images/deployment/creation_images_ecr.png)


Documentacion de arquitectura
- https://www.cosmicpython.com/book/chapter_06_uow.html

Repositorio github original
- https://github.com/cosmicpython/code.git


alembic revision --autogenerate -m "migration"

