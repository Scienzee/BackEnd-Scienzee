from Users.models import AreaAtuacao

"""
Script para cadastrar Disciplinas/Área de Atuação/Área de preferencia
python manage.py shell
exec(open('scripts/AreadeAtuacao.py').read())
"""

def validate(objArea):
    try:
        objAreaAtuacao = AreaAtuacao.objects.get(nome__icontains = objArea)
        if objAreaAtuacao:
            return False
        else:
            return True
    except:
        return True

def registrar_Area():
    listAreas = ["Matemática", "Probabilidade e Estatística", "Ciência da Computação", "Astronomia", "Física", "Química", 
                "Geociências", "Oceanografia", "Genética", "Botânica", "Zoologia", "Ecologia", "Morfologia", "Fisiologia", "Bioquímica",
                "Biofísica", "Farmacologia", "Imunologia", "Microbiologia", "Parasitologia", "Linguística" , "Letras", "Artes", "Filosofia",
                "Sociologia", "Antropologia", "Arqueologia", "História", "Geografia", "Psicologia","Educação", "Ciência política", "Teologia"
                "Turismo", "Desenho industrial", "Economia doméstica", "Serviço social", "Comunicação", "Museologia", "Ciência da informação", 
                "Demografia", "Planejamento urbano e regional", "Arquitetura e urbanismo", "Economia", "Administração", "Direito", 
                "Ciência e tecnologia de alimentos", "Recursos pesqueiros e engenharia de pesca", "Medicina veterinária", "Zootecnia", "Engenharia agrícola", 
                "Recursos florestais e engenharia florestal", "Agronomia", "Educação física", "Fisioterapia e terapia ocupacional", "Fonoaudiologia", "Saúde coletiva",
                "Nutrição", "Enfermagem", "Farmácia", "Odontologia", "Medicina", "Engenharia biomédica", "Engenharia aeroespacial", 
                "Engenharia naval e oceânica", "Engenharia de transportes", "Engenharia nuclear", "Engenharia de produção", "Engenharia sanitária", 
                "Engenharia química", "Engenharia mecânica", "Engenharia elétrica", "Engenharia de materiais e metalúrgica", "Engenharia de minas", "Engenharia civil",]
    for area in listAreas:
        if validate(area):
            objAreaAtuacao = AreaAtuacao()
            objAreaAtuacao.nome = area
            objAreaAtuacao.save()
            print(f"{area} foi registrado com sucesso!")
        else:
            print(f"{area} já está registrado no sistema!")
registrar_Area()