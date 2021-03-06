from django.db import models
try:
    # django < 1.10
    from django.core.urlresolvers import reverse
except ImportError:
    # django >= 1.10
    from django.urls import reverse
from django.utils.translation import ugettext_lazy as __


class BusinessRuleModel(models.Model):
    name = models.TextField(unique=True, verbose_name=__('name'))
    description = models.TextField(blank=True, verbose_name=__('description'))
    rule_data = models.TextField(verbose_name=__('rule data'))
    rules = models.TextField(verbose_name=__('rules'), default={})

    def get_absolute_url(self):
        return reverse('dbr:business-rule-form', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
