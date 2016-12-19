from django.conf.urls import url
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView

from hordak.views.accounts import AccountListView, AccountCreateView, AccountUpdateView
from hordak.views.transactions import TransactionCreateView

from battlecat.accounts.apps import AccountsConfig
from . import views

urlpatterns = [
    url(r'^$', AccountListView.as_view(
        template_name='accounts/account_list.html'
    ), name='list'),

    url(r'^create/$', AccountCreateView.as_view(
        template_name='accounts/account_create.html',
        success_url=reverse_lazy('accounts:list'),
    ), name='create'),

    url(r'^update/(?P<uuid>.+)/$', AccountUpdateView.as_view(
        template_name='accounts/account_update.html',
        success_url=reverse_lazy('accounts:list'),
    ), name='update'),
]
