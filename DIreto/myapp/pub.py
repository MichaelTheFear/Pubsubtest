from . import models
import random

def envia_email(email:str, titulo:str):
    print(f" Enviando email para {email} com o titulo {titulo}")

def envia_push(nome:str, titulo:str):
    print(f" Enviando push para {nome} com o titulo {titulo}")




def gera_usuarios_e_categorias():
    # cria 5 categorias
    categorias = ["Seminario", "Estagio", "Monitoria", "Projeto", "Palestra"]
    cat_aleatoria = lambda : random.choice(categorias)
    """
    for categoria in categorias:
        models.Categoria(nome=categoria).save()
    """


    for nome in ["Joao", "Maria", "Jose", "Ana", "Pedro"]:
        # notificar por email e push 50% de chance de ser True
        user = models.Usuario(nome=nome, email=f"{nome}@email.com",
                senha="123456", matricula="1234567",
                notificacao_por_email=random.choice([True, False]),
                notificacao_por_push=random.choice([True,False]))
        
        user.save()
        #adiciona uma categoria aleatoria ao usuario
        user.categoria.add(models.Categoria.objects.get(nome=cat_aleatoria()))
        
        
    

def pub(categoria:str,post:models.Postagem):
    # query todos os usuarios que tem a categoria (MANY TO MANY)
    usuarios = models.Usuario.objects.all().filter(categoria=categoria)
    # pegar todos os emails dos usuarios que tenham notificacao_por_email = True
    emails = [usuario.email for usuario in usuarios if usuario.notificacao_por_email]
    for email in emails:
        envia_email(email, models.Postagem.titulo)

    # pegar todos os tokens dos usuarios que tenham notificacao_por_push = True
    nomes = [usuario.nome for usuario in usuarios if usuario.notificacao_por_push]
    for nome in nomes:
        envia_push(nome, models.Postagem.titulo)

    
    post.save()
    post.categoria.add(models.Categoria.objects.get(nome=categoria))
