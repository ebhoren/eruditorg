# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views


urlpatterns = [
    url(_(r'^(?P<key>[\w-]+)/$'), views.AccountActionLandingView.as_view(), name='landing'),
    url(_(r'^(?P<key>[\w-]+)/c/$'), views.AccountActionConsumeView.as_view(), name='consume'),
]
