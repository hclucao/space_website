"""para manter o código mais limpo. um boa prática, 
seia deixar a responsabilidade das urls de um app, 
dentro do proprio app. e passar penas a include do app na urls do stup"""

from django.contrib import admin
from django.urls import path, include #include importa a urls.py de cada app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')) #usando o include para inportar as urls de um app
]
