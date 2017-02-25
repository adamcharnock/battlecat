"""battlecat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from hordak.views import accounts
from hordak.views import transactions


hordak_urls = [
    url(r'^transactions/create/$', transactions.TransactionCreateView.as_view(), name='transactions_create'),
    url(r'^transactions/reconcile/$', transactions.TransactionsReconcileView.as_view(), name='transactions_reconcile'),
    url(r'^$', accounts.AccountListView.as_view(), name='accounts_list'),
    url(r'^accounts/create/$', accounts.AccountCreateView.as_view(), name='accounts_create'),
    url(r'^accounts/update/(?P<uuid>.+)/$', accounts.AccountUpdateView.as_view(), name='accounts_update'),
    url(r'^accounts/(?P<uuid>.+)/$', accounts.AccountTransactionsView.as_view(), name='accounts_transactions'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include(hordak_urls, namespace='hordak', app_name='hordak')),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
