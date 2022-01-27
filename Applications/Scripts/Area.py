from django.contrib.auth.models import Group
from Users.models import Area

# Arquivo para cadastrar as grandes áreas

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

"""
Docker
sudo docker-compose exec web python manage.py shell

Virtual Env
python manage.py shell
exec(open('Applications/Scripts/Area.py').read())
"""

def validate(nameArea):
    try:
        validar = Area.objects.get(name = nameArea)
        if validar:
            return False
        else:
            return True
    except:
        return True


listAreas = {
    'Area':
    [
        {
            'name': 'Ciências Exatas e da Terra',
            'image': 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name': 'Ciências Biológicas',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name' : 'Engenharias',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name' : 'Ciências da Saúde',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name': 'Ciências Agrárias',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name': 'Ciências Sociais Aplicadas',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name' : 'Ciências Humanas',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
        {
            'name': 'Linguística, Letras e Artes',
            'image' : 'https://s1.static.brasilescola.uol.com.br/be/vestibular/bb29a29f2d3ae710569ea2ff56939ccf.jpg',
        },
    ],
}
print(BOLD + "\nFoi iniciado a geração de registros das areas!\n" + RESET)

for area in listAreas['Area']:
    name =  area['name']
    image =  area['image']

    if validate(area):
        objArea = Area()
        objArea.name = name
        objArea.image =  image
        objArea.save()
        print(GREEN + "A Área" + RESET + BOLD + f" {area} " + RESET + GREEN + "foi registrado com sucesso no sistema!" + RESET)
    else:
        print(RED + "A Área" + RESET + BOLD + f" {area} " + RESET + RED + "já está registrado no sistema!" + RESET)
