from django.urls import path

from . import views


urlpatterns = [
     path('', views.index, name='index'),
]
urlpatterns += [
    path('', views.cotiza_ahora, name='cotiza_ahora'),
]

urlpatterns += [
    path('', views.CotizaInstanceCreate.as_view(), name='cotiza_create'),
    path('', views.CotizaInstanceUpdate.as_view(), name='cotiza_update'),
    path('', views.CotizaInstanceDelete.as_view(), name='cotiza_delete'),
]