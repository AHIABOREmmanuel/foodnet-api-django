
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Categorie', CategorieViewSet)
router.register('Plat', PlatViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
 
]