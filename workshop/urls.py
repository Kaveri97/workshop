from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import Home
from registration.urls import *
from workshop.views import *
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'workshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'register/login.html'},
        name='login'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'register/logout.html'},
        name='logout'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^register/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls))

]
