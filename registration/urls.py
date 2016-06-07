from django.conf.urls import include, url
from registration.views import *

from registration.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^chocolate/add', AddChocolateView.as_view(), name='add_chocolate'),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='edit'),

]