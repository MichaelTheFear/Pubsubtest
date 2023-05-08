from django.http import HttpResponse
from . import pub
from . import models
from random import randint

#pub.gera_usuarios_e_categorias()
#http://127.0.0.1:8000/?categoria=Seminario&titulo=Meu%20seminario

def index(request):
    id=randint(0, 100)

    try:
        titulo=request.GET.get("titulo")
        categoria=request.GET.get("categoria")

        pub.pub(categoria, models.Postagem(id, titulo=titulo, conteudo=titulo,
                            usuario=models.Usuario.objects.get(email="Joao@email.com"),
                               data_do_evento="2021-05-06 22:59:00"))
    except:
        pass

    posts = models.Postagem.objects.all()
    resposta = ""
    for post in posts:
        resposta += f"{post.titulo} <br> "
    
    resposta+="\n\n numero de posts: "+str(len(posts))
    return HttpResponse(resposta)
