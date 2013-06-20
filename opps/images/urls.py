#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.decorators.cache import cache_page

from .views import ImageDetail

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)$',
        cache_page(settings.OPPS_CACHE_EXPIRE_DETAIL)(
            ImageDetail.as_view()), name='open'),
)
