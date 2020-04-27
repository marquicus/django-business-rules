from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DbrAppConfig(AppConfig):
    name = 'django_business_rules'
    verbose_name = _('Business Rules')
