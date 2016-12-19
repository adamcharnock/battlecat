from django.conf.urls import url
from django.views.generic.base import TemplateView
from hordak.views.transactions import TransactionCreateView

from . import views

urlpatterns = [
    url(r'^create/$', TransactionCreateView.as_view(template_name='transactions/create_transaction.html', success_url='/'), name='create')
]
