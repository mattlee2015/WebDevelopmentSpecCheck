from django.conf.urls import url
from django.contrib.auth import views as auth_views #not to mix up with my own views
from . import views

app_name = 'accounts'

urlpatterns = [
    #connect to template name
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),

    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),

    url(r'signup/$',views.SignUp.as_view(),name='signup'),

    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

]
