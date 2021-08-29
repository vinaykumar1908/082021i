from django.urls import path, include
from rakes import views

urlpatterns = [
    path('', views.RakesHomePageView.as_view(), name='Rakes_home'),
    path('RakeEntry', views.AddRake, name='Rakes_entry'),
    path('ModuleAutocomplete', views.autocomplete1, name='autocomplete1'),
    path('AddModule', views.AddModule, name='AddModule'),
]
