from Users.models import AreaAtuacao

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

"""
Script para cadastrar Disciplinas/Área de Atuação/Área de preferencia
python manage.py shell
exec(open('scripts/AreadeAtuacao.py').read())
"""


listSubAreas = {
    'Ciências Exatas e da Terra': 
    [
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Análise',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Geometria e Topologia',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Matemática Aplicada',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },       
        {
            'name': 'Probabilidade',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Estatística',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Probabilidade e Estatística Aplicadas',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Teoria da Computação',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Matemática da Computação',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Metodologia e Técnicas da Computação',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Sistemas de Computação',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Astronomia de Posição e Mecânica Celeste',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Astrofísica Estelar',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Astrofísica do Meio Interestelar',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Astrofísica Extragaláctica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Astrofísica do Sistema Solar',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Instrumentação Astronômica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Física Geral',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Áreas Clássicas de Fenomenologia e suas Aplicações',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Física das Partículas Elementares e Campos',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Física Nuclear',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Física Atômica e Molecular',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Física dos Fluídos, Física de Plasmas e Descargas Elétricas',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Física da Matéria Condensada',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Química Orgânica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Química Inorgânica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Físico-Química',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Química Analítica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Geologia',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Geofísica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Meteorologia',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Geodésia',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Geografia Física',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Oceanografia Biológica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Oceanografia Física',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Oceanografia Química',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Oceanografia Geológica',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        {
            'name': 'Álgebra',
            'image': 'https://static.semrush.com/blog/uploads/media/39/4f/394f92fd06792246f5833d1ab3c05c4d/reverse-image-search.svg',
        },
        '', 
        'Análise',
        'Geometria e Topologia',
        'Matemática Aplicada', 
        'Probabilidade',
        'Estatística',
        'Probabilidade e Estatística Aplicadas',
        'Teoria da Computação',
        'Matemática da Computação',
        'Metodologia e Técnicas da Computação', 
        'Sistemas de Computação',
        'Astronomia de Posição e Mecânica Celeste',
        'Astrofísica Estelar', 
        'Astrofísica do Meio Interestelar',
        'Astrofísica Extragaláctica',
        'Astrofísica do Sistema Solar', 
        'Instrumentação Astronômica',
        
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
        'Álgebra', 
        'Análise',
        'Geometria e Topologia',
    ],
    'Ciências Biológicas':
    [
        'Sistema web',
    ],
    'Engenharias':
    [
        'Pesquisa Científica',
        'Fomento',
    ],
    'Ciências da Saúde':
    [
        'Sistema web',
    ],
    'Ciências Agrárias':
    [
        'Sistema web',
    ],
    'Ciências Sociais Aplicadas':
    [
        'Sistema web',
    ],
    'Ciências Humanas':
    [
        'Sistema web',
    ],
    'Linguística, Letras e Artes':
    [
        'Sistema web',
    ],
}









