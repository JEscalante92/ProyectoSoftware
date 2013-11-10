# -*- encoding: utf-8 -*-
import django_filters
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
	username = django_filters.CharFilter(lookup_type='istartswith')
	class Meta:
		model = User
		fields = ['username']