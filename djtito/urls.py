from django.contrib import admin
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView, RedirectView

from djauth.views import loggedout

admin.autodiscover()

handler404 = 'djtools.views.errors.four_oh_four_error'
handler500 = 'djtools.views.errors.server_error'

urlpatterns = [
    # auth
    url(
        r'^accounts/login/$',auth_views.login,
        {'template_name': 'accounts/login.html'},name='auth_login'
    ),
    url(
        r'^accounts/logout/$',auth_views.logout,
        {'next_page': reverse_lazy("auth_loggedout")},
    ),
    url(
        r'^accounts/loggedout/', loggedout,
        {'template_name': 'accounts/logged_out.html'}
    ),
    #/djtito/accounts/login/
    url(
        r'^accounts/$',
        RedirectView.as_view(url=reverse_lazy('auth_login'))
    ),
    #admin
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    # bridge
    url(
        r'^newsletter/',
        include('djtito.newsletter.urls')
    ),
    #/djtito/newsletter/manager/
    url(
        r'^$',
        RedirectView.as_view(url=reverse_lazy('newsletter_manager'))
    ),
]
