
class virtualenv():

    ##estabeleça um ambiente virtual dentro do diretório do projeto
    def linux_ou_MacOS()->str:
        return "virtualenv -p python3 venv"

    def Windows()->str:
        return 'python -m virtualenv venv'

    ##ativar ambiente virtual
    def Linux_ou_MacOS()->str:
        return 'source venv/bin/activate'

    def Windows()->str:
        return 'source venv/Scripts/activate'

class django_command():
    def Crie_o_projeto_Django()->str:
        return 'django-admin startproject setup .'

    def Rode_o_servidor()->str:
        return 'python manage.py runserver'

env = [
    { 
        'atualizar requiriments.txt':  'pip freeze > requirements.txt'
    },
    {
        'criar env': 'virtualenv -p python3 venv'
    },
    {
        'ativar env': 'source venv/bin/activate'
    }
]

django = [
    #criar coisas
    {
        'criar projeto' : 'django-admin startproject setup .',

        #um projeto pode conter diversos apps, e asão são funcionalidades dentro de um projeto
        'criar app' : 'django-admin startapp <nome do app>'

        #roda um comando para o djando achar os arquivos staticos e endereçar eles para serem usados
        'arquivos stataticos' : 'python manage.py collectstatic'
    },

    #HTTP     URL
    {
        #importar o modulo que nos permite responder a uma requisição do cliente ao servidor
        'importar response' : 'from django.http import HttpResponse' 
    },

]