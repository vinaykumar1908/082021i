from django.urls import path, include
from exams import views

urlpatterns = [
    path('', views.ExamHomePageView.as_view(), name='Exams_home'),
    path('STR/', views.STRHomePageView.as_view(), name='STR_home'),
    path('CC/', views.CCHomePageView.as_view(), name='CC_home'),
    #path('ModuleAutocomplete', views.autocomplete1, name='autocomplete1'),
    #path('AddModule', views.AddModule, name='AddModule'),
    #path('ShowRakes', views.RakeListView.as_view(), name='Rake_list'),
    #path('ShowRakeDetail/<int:pk>/',
    #     views.RakeDetailView.as_view(), name='Rake_detail'),
    #path('ShowModule', views.ModuleListView.as_view(), name='Module_list'),
    #path('ShowModuleDetail/<int:pk>/',
    #     views.ModuleDetailView.as_view(), name='Module_detail'),
    #path('ModuleList/<int:pk>/edit/',
    #     views.ModuleEditView.as_view(), name='Module_edit'),
    #path('RakeList/<int:pk>/edit/',
    #     views.RakeEditView.as_view(), name='Rake_edit'),
    #path('moduleName', views.moduleName, name='moduleName'),
    #path('ModuleQuickLink2', views.ModuleDetailLink, name='ModuleDetailLink2'),
    #path('ModuleQuickLink3', views.ModuleDetailLink3, name='ModuleDetailLink3'),
    #path('RakeDetailLink2', views.RakeDetailLink2, name='RakeDetailLink2'),
    #path('RakeDetailLink3', views.RakeDetailLink3, name='RakeDetailLink3'),
    #path('WagonDetailLink', views.WagonDetailLink, name='WagonDetailLink'),
    #path('wagonnumberlink', views.wagonnumberlink, name='wagonnumberlink'),
]
