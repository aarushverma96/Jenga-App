from django.conf.urls import include,url
from . import views

# urlpattern starts here...
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login$', views.login_jenga, name='login_jenga'),
]
