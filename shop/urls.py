
from django.urls import path
from.import views

urlpatterns = [

    path("", views.index,name='homepage'),
    path("about/", views.about,name='about page'),
    path("contact/", views.contact,name='contact page'),
    path("tracker/", views.tracker,name='tracker page'),
    path("search/", views.search,name='search page'),
    path("products/<int:myid>", views.productView,name='productview page'),
    path("checkout/", views.checkout,name='checkout page'),
]