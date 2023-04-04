from django.urls import path
from  .views import CompanyCreateView, CompanyUpdateView, CompanyDeleteView


urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='company-create'),
    path('update/<int:pk>/', CompanyUpdateView.as_view(), name='company-update'),
    path('delete/<int:pk>/', CompanyDeleteView.as_view(), name='company-delete'),
]