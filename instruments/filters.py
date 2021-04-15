from .models import Customer, Instrument, InstrumentModels
import django_filters
from django import forms
from django.db import models
from django_filters import DateRangeFilter, DateRangeFilter
from django_filters.widgets import RangeWidget

class InstrumentFilter(django_filters.FilterSet):

    date_range = DateRangeFilter(field_name='date')
    class Meta:
        model = Instrument
        fields = ['serial_number', 'instrument_model', 'owner', 'location',
        'cal_due', 'status', 'contam_status']
        exclude = []
        filter_overrides ={
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra':lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra':lambda f: {
                    'widget' : forms.CheckboxInput,
                },
            },
            models.DateField: {
                'filter_class': django_filters.DateRangeFilter,
                'extra':lambda f: {
                    # 'widget' : forms.DateInput,
                    # 'widget': forms.DateInput,
                    'widget': RangeWidget(attrs={'type': 'date'})
                },
            }
        }


# class RecieveFilter(django_filters.FilterSet):

#     date_range = DateRangeFilter(field_name='date')
#     class Meta:
#         model = Instrument
#         fields = ['serial_number', 'owner',  'status']
#         exclude = []
#         filter_overrides ={
#             models.CharField: {
#                 'filter_class': django_filters.CharFilter,
#                 'extra':lambda f: {
#                     'lookup_expr': 'icontains',
#                     'widget': CsvWidget(),
#                 },
#             },
#             models.BooleanField: {
#                 'filter_class': django_filters.BooleanFilter,
#                 'extra':lambda f: {
#                     'widget' : forms.CheckboxInput,
#                 },
#             },
#             models.DateField: {
#                 'filter_class': django_filters.DateRangeFilter,
#                 'extra':lambda f: {
#                     # 'widget' : forms.DateInput,
#                     # 'widget': forms.DateInput,
#                     'widget': RangeWidget(attrs={'type': 'date'})
#                 },
#             }
#         }