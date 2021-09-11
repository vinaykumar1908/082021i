from django.urls import path, include
from staff import views

urlpatterns = [
    path('', views.StaffHomePageView.as_view(), name='Staff_home'),
    path('GangEntry', views.AddGang2, name='Gangs_entry'),
    path('StaffAutocomplete', views.autocomplete1, name='autocomplete11'),
    path('AddStaff', views.AddStaff2, name='AddStaff'),
    path('ShowGang', views.GangListView.as_view(), name='Gang_list'),
    path('ShowGangDetail/<int:pk>/',
         views.GangDetailView.as_view(), name='Gang_detail'),
    path('ShowStaff', views.StaffListView.as_view(), name='Staff_list'),
    path('ShowStaffDetail/<int:pk>/',
         views.StaffDetailView.as_view(), name='Staff_detail'),
    path('StaffList/<int:pk>/edit/',
         views.StaffEditView.as_view(), name='Staff_edit'),
    path('GangList/<int:pk>/edit/',
         views.GangEditView.as_view(), name='Gang_edit'),
    path('staffName', views.staffName, name='staffName'),
    path('staffQuickLink2', views.StaffDetailLink, name='StaffDetailLink2'),
    path('staffQuickLink3', views.StaffDetailLink3, name='StaffDetailLink3'),
    path('GangDetailLink2', views.GangDetailLink2, name='GangDetailLink2'),
    path('RakeDetailLink3', views.GangDetailLink3, name='GangDetailLink3'),
]
