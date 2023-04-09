from django.urls import path
from  .views import CompanyCreateView, CompanyUpdateView, CompanyDeleteView, JoinCompanyAPIView, UpdateCompanyCodeView


urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='company-create'),
    path('update/<int:pk>/', CompanyUpdateView.as_view(), name='company-update'),
    path('delete/<int:pk>/', CompanyDeleteView.as_view(), name='company-delete'),
    path('add-user-to-company/', JoinCompanyAPIView.as_view(), name='add_user_to_company'),
    path('update-code/', UpdateCompanyCodeView.as_view(), name='update_company_code'),
]