from django.urls import include, re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    re_path(r'^departments$',views.departmentApi),
    re_path(r'departments/([0-9]+)$',views.departmentApi),

    re_path(r'^employees$',views.employeeApi),
    re_path(r'employees/([0-9]+)$',views.employeeApi),

    re_path(r'^employees/savefile',views.SaveFile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)