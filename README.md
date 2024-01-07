# Adote

Aula pythonando-programming-path

## Comece por aqui

Vou assumir que para chegar ate aqui você já tenha o python instalado no seu PC. Portanto, ao clonar o projeto, primeiro execute o comando; `python -m venv venv` - para criar o ambiente virtual.

> Se estiver usando o PowerShel do Windows, vai ser importante lembrar de que primeiro deve executar o comando; `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` - para que ele possa reconhecer alguns comandos necessários ao projeto.

Feito isso, certifique-se de **ativar** o ambiente virtual criado, execute o comando; `.\venv\Scripts\activate.ps1` - para ativar o ambiente.

> **Instalando as Dependencias do Projeto**: Lembre-se de rodar o comando `pip install -r requirements.txt`, aguarde a instalação completar. 

> **Importante Lembrar**: Nunca enviamos a `SECRET_KEY` para o Github, portanto vamos precisar fazer uma cópia do arquivo `.env_exemplo`, renomear a cópia para `.env` apenas, e dentro desse arquivo criar uma chave de segurança lá.

Outro detalhe importante, nunca enviamos o arquivo do banco de dados para o Github tambem, portanto, vai ser necessário agora rodar as migrações para criar todas as tabelas localmente no seu DB. Execute o comando a seguir `python manage.py migrate`, aguarde as tabelas serem criadas localmente.

Repara que seu banco de dados local acabou de ser criado, portanto, não existe nenhum usuario cadastrado. Vamos resolver isso. Execute o comando `python manage.py createsuperuser`.

## Estrutura do Projeto

    requirements.txt    # Dependencias do projeto aqui.
    **core/**
        env_exemplo  # Ninguem é obrigado a adivinhar as variaveis de ambiente, seguem aqui.
        settings.py  # Configurações gerais do projeto aqui.
        urls.py  # Mapeamento das rotas do projeto aqui.
    **divulgar/**
        **templates/**
            novo_pet.html  # Exibe o form de cadastro para incluir novo pet no sistema.
            seus_pets.html  # Lista os pets do usuario logado no sistema.
        admin.py  # Coordena o registro do app divulgar no painel admin do django.
        models.py  # Responsável por todas as tabelas do app divulgar no banco de dados.
        urls.py  # Mapeamento das rotas do app divulgar aqui.
        views.py  # Trata da lógica de processamento das requisições HTTP.
    **documentacao/**
        **docs/**
            index.md  # Informações base sobre a construção desse projeto.
        mkdocs.yml  # Arquivo de configuração usado pelo MkDocs.
    **media/**
        **fotos_pets/**
            # Local onde é armazenado as fotos de uploads feito pelo usuario ao cadastrar o pet.
    