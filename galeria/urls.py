"""para manter o código mais limpo. um boa prática, 
seia deixar a responsabilidade das urls de um app, 
dentro do proprio app. e passar penas a include do app na urls do stup"""

from django.urls import path
from galeria.views import index, image

urlpatterns = [
    path('', index, name = 'index'),
    path('image/', image, name = 'image') # foi necessário passar um ID para esse caminha. para que podemos especificar ele usando o {%url 'id'%} no html 
]
