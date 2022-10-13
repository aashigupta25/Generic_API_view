from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Empinfo/', views.EmployeeList.as_view()),
    path('Empcreate/', views.EmployeeCreate.as_view()),
    path('Empinfo/<int:pk>', views.EmployeeRetrieve.as_view()),
    path('Empinfo-update/<int:pk>', views.EmployeeUpdate.as_view()),
    path('Empinfo-delete/<int:pk>', views.EmployeeDelete.as_view()),
    path('Empinfo-list-create/', views.EmployeeListCreate.as_view()),
    path('Empinfo-retrieve-update-destroy/<int:pk>', views.EmployeeRetrieveUpdateDestroy.as_view())
]