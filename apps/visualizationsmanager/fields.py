"""
Provides custom serializer fields
"""
__author__ = 'mmilaprat'
from rest_framework import serializers
from rest_framework.serializers import ValidationError,  WritableField, SlugRelatedField

from django.core.exceptions import ObjectDoesNotExist

from .adapter import *

import datetime

class DatasetsField(serializers.WritableField):

    def field_to_native(self, obj, field_name):
        ids = getattr(obj, self.source).all()
        result = []

        datasets = DatasetsAdapter()

        for i in ids:
            temporal = datasets.get(i.id)
            result.append(temporal)

        return result

    def from_native(self, value):
        if not type(value) is list:
            raise ValidationError("Datasets property is not a list")
        return value


class HistoricalEventsField(serializers.WritableField):

    def field_to_native(self, obj, field_name):
        ids = getattr(obj, self.source).all()
        result = []
        historical_events = HistoricalEventsAdapter()

        for i in ids:
            temporal = historical_events.get(i.id)
            result.append(temporal)
        return result

    def from_native(self, value):
        if not type(value) is list:
            raise ValidationError("Historical event property is not a list")
        return value


class VisualizationTitleField(serializers.WritableField):

    def field_to_native(self, obj, field_name):
        result = obj.visualization.title
        return result

    def from_native(self, value):
        if not type(value) is list:
            raise ValidationError("Visualization is not a list")
        return value

class PolicyDomainSlugRelatedField(SlugRelatedField):

    def to_internal_value(self, data):
        i = 5
        pass    
