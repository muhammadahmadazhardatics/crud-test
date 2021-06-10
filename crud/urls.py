from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from crudtest import views

router = routers.DefaultRouter()
router.register("crud", views.CrudViewSet, basename="crud")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('search/', views.SearchWithParams.as_view(), name='firstname'),
]