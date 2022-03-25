from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^search/', views.search_for_businesses, name='search_results'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/login', views.login, name='login')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)