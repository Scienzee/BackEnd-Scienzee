from Administration.models import TypesPublication

'''
Código para executar o script de cadastro do tipo de categoria que a plataforma oferecerá
$ python manage.py shell
$ exec(open('Applications/Scripts/PublicationCategory.py').read())
'''

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


listTypesPublication = {
    'category':
    [
        {
            'name': 'Artigo',
            'descreption': 'Artigos das mais diversas areas! Tudo para facilitar sua vida academica e profissional',
            'icons' : 'article',
        },
        {
            'name': 'Notícias',
            'descreption': 'Sobre o mundo profissional e academico para se manter atualizado!',
            'icons' : 'feed',
        },
    ],
}

def validar(name):
    try:
        TypesPublication.objects.get(name=name)
        return False
    except:
        return True


print(BOLD + "\nFoi iniciado a geração de Categorias do Registros!\n" + RESET)
for category in listTypesPublication['category']:
    name = category['name']
    descreption = category['descreption']
    icons = category['icons']
    if validar(name):
        objTypesPublication = TypesPublication()
        objTypesPublication.name = name
        objTypesPublication.descreption = descreption
        objTypesPublication.icons = icons
        objTypesPublication.save()
        print(GREEN + "O grupo" + RESET + BOLD + f" {category} " + RESET + GREEN + "foi registrado com sucesso no sistema!" + RESET)
    else:
        print(RED + "O grupo" + RED + RED + f" {category} " + RED + RED + "já está registrado no sistema!" + RESET)