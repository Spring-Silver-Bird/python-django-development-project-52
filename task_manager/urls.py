from django.contrib import admin
from django.urls import include, path
from task_manager import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("users/", include(("task_manager.users.urls","users"), namespace="users")),
    path("statuses/", include(("task_manager.statuses.urls","statuses"), namespace="statuses")),
    path('login/', views.UserLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
