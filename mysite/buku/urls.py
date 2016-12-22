from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.buku_list, name='buku_list'), #alias URL halaman utama
    url(r'^(?P<pk>\d+)/', views.buku_detail, name='buku_detail'), #alias URL detil buku
	url(r'^map-vis', views.map_vi, name='map_vi'), #alias URL tampilan peta lokasi penerbit
]


