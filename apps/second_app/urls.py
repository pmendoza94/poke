from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokes$', views.pokes),
    url(r'^poke_proccesser$', views.poke_proccesser),
    url(r'^add_poke$', views.add_poke),
]
