#!/usr/bin/env python
# -*- coding: utf-8 -*-
from opps.articles.views.generic import OppsDetail

from ..models import Image


class ImageDetail(OppsDetail):
    model = Image
    type = 'images'

    @property
    def queryset(self):
        self.site = get_current_site(self.request).domain
        self.long_slug = self.kwargs['tag']
        self.article = self.model.objects.filter(
            site_domain=self.site,
            tags__slug=self.long_slug,
            date_available__lte=timezone.now(),
            published=True).all()
        return self.article