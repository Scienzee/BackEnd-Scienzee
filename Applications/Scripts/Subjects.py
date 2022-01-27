from Users.models import AreaAtuacao

"""
Script para cadastrar Disciplinas/Área de Atuação/Área de preferencia
python manage.py shell
exec(open('scripts/AreadeAtuacao.py').read())
"""


listSubAreas = {
    'Ciências Exatas e da Terra': 
    [
        'Álgebra', 
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

def validar(objName):
    try:
        l = SubMatter.objects.get(name=objName)
        return False
    except:
        return True


for matter in listSubMatters: #Percorrendo um for na minha lista de Matters 
    objMatter = Matter.objects.get(name=matter)
    for objSubMatter in listSubMatters[matter]: #Percorendo um for dentro da minha lista de subMatters 
        if validar(objSubMatter):
            objSubMatterInst = SubMatter() #Instancia minha classe SubMatter
            objSubMatterInst.name = objSubMatter #Criando minha SubMatters
            objSubMatterInst.matter = objMatter
            objSubMatterInst.is_active = True
            objSubMatterInst.save()
            print(f"A SubMatter {objSubMatterInst.name} foi cadastrada com sucesso!")
        else:
            print(f'A SubMatter {a} já foi cadastrada...')
    print("##########################################\n\n\n")





