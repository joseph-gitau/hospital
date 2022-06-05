from django.urls import path
# importing views from views
from .views import EmployeeCreateViewOld,EmployeeListView,EmployeeDetailView,EmployeeUpdateView,EmployeeDeleteView, SignUpView



urlpatterns = [
    path('employee/create', SignUpView.as_view(), name='employee-create'),
    path('employees', EmployeeListView.as_view(), name='employees-list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),


]