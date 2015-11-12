from django.conf.urls import patterns, url

urlpatterns = patterns(
    'contatos.views',

    url(r'^$', 'home', name='home'),
)
