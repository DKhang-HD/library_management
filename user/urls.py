from django.urls import path
from .views import homepage, SignUpView, permission_request

app_name = 'User'

urlpatterns = [
    path("", homepage, name="homepage"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("permission/<int:user_id>/", permission_request, name="permission"),
    # path("", views.homepage, name="homepage"),
    # path("login/", views.login_request, name="login"),
    # path("register/", views.register_request, name="register"),
    # path("logout/", views.logout_request, name="logout"),

]