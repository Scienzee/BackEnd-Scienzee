from Users.models import CategoriaPublicacao

'''
Código para executar o script de cadastro do tipo de categoria que a plataforma oferecerá
$ python manage.py shell
$ exec(open('scripts/CategoriasdePublicacao.py').read())
'''

listCategoriaPublicacao = {
    'categoria':
    [
        {
            'nome': 'Artigo',
            'resumo': 'Artigos das mais diversas areas! Tudo para facilitar sua vida academica e profissional',
            'icone' : 'article',
        },
        {
            'nome': 'Notícias',
            'resumo': 'Sobre o mundo profissional e academico para se manter atualizado!',
            'icone' : 'feed',
        },
        {
            'nome': 'Podcast',
            'resumo': 'Os mais diversos podcast com o intuito de levar a melhor educação possível até voce!',
            'icone' : 'podcasts',
        },
        {
            'nome': 'Documentário',
            'resumo': 'Documentários diversificado! A sensação é de estar assistindo a série do momento!',
            'icone' : 'live_tv',
        },
    ],
}


def validar(valor):
    try:
        CategoriaPublicacao.objects.get(nome=valor)
        return False
    except:
        return True



for categoria in listCategoriaPublicacao['categoria']:
    nome = categoria['nome']
    resumo = categoria['resumo']
    icone = categoria['icone']

    if validar(nome):
        objCategoriaPublicacao = CategoriaPublicacao()
        objCategoriaPublicacao.nome = nome
        objCategoriaPublicacao.resumo = resumo
        objCategoriaPublicacao.icone = icone
        objCategoriaPublicacao.save()
    
        print(f'Categoria = {nome} foi CADASTRADA!!')
    else:
        print(f'A Categoria usuario = {nome} já esta cadastrada!!')