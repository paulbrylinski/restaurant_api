from django.urls import path
from employees import views as employees_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/employees/', employees_views.employee_list),
    path('api/employees/<int:pk>/', employees_views.employee_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)