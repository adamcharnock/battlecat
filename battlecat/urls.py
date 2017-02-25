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

from hordak import views as hordak_views


hordak_urls = [
    url(r'^transactions/create/$', hordak_views.TransactionCreateView.as_view(), name='transactions_create'),
    url(r'^transactions/reconcile/$', hordak_views.TransactionsReconcileView.as_view(), name='transactions_reconcile'),
    url(r'^$', hordak_views.AccountListView.as_view(), name='accounts_list'),
    url(r'^accounts/create/$', hordak_views.AccountCreateView.as_view(), name='accounts_create'),
    url(r'^accounts/update/(?P<uuid>.+)/$', hordak_views.AccountUpdateView.as_view(), name='accounts_update'),
    url(r'^accounts/(?P<uuid>.+)/$', hordak_views.AccountTransactionsView.as_view(), name='accounts_transactions'),

    url(r'^import/$', hordak_views.CreateImportView.as_view(), name='import_create'),
    url(r'^import/(?P<uuid>.*)/setup/$', hordak_views.SetupImportView.as_view(), name='import_setup'),
    url(r'^import/(?P<uuid>.*)/dry-run/$', hordak_views.DryRunImportView.as_view(), name='import_dry_run'),
    url(r'^import/(?P<uuid>.*)/run/$', hordak_views.ExecuteImportView.as_view(), name='import_execute'),
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
