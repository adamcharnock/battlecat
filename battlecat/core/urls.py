from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
#    url(r'^page/$', views.myview),
    url(r'^$', TemplateView.as_view(template_name='core/test.html'))
]
