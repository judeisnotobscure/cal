from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from instruments.models import Customer, InstrumentModels, Instrument, InstrumentType,Location
from instruments.models import Status, ContamStatus

# Register your models here.
admin.site.register(Instrument)
admin.site.register(Customer)
admin.site.register(InstrumentModels)

admin.site.register(InstrumentType)
admin.site.register(Location)
admin.site.register(Status)
admin.site.register(ContamStatus)