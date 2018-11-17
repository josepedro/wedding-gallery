from django.conf.urls import url
from django.contrib.auth import views as auth_views

from weddinggallery.core import views

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^change_status_photo/$', views.change_status_photo, name='change_status_photo'),
    url(r'^$', views.PhotoCreateView.as_view(), name='home'),
]
