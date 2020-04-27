from django.conf.urls import url
from django_business_rules.views import BusinessRuleFormView, BusinessRuleListView


app_name = 'dbr'
urlpatterns = [
    url(r'^business-rule/$', BusinessRuleListView.as_view(), name='business-rule-list'),
    url(r'^business-rule/(?P<pk>[0-9]+)/$', BusinessRuleFormView.as_view(), name='business-rule-form'),
]
