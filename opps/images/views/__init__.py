#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.sites.models import get_current_site
from django.utils import timezone

from opps.articles.views.generic import OppsDetail

from ..models import Image


class ImageDetail(OppsDetail):
    model = Image
    type = 'images'
    template_name_suffix = '_images'

    @property
    def queryset(self):
        self.site = get_current_site(self.request).domain
        self.long_slug = self.kwargs.get('slug')
        self.image = self.model.objects.filter(
            slug=self.kwargs.get('slug'),
            date_available__lte=timezone.now(),
            published=True)[0]
