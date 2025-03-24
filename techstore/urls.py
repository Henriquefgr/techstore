from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),  
]
handler404 = 'produtos.views.custom_404'
handler500 = 'produtos.views.custom_500'