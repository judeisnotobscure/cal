from django import forms
from .models import Instrument, InstrumentModels, Customer, Location, ContamStatus
from django.core import validators




class AddInstrument(forms.ModelForm):
    serial_number = forms.CharField()
    instrument_model = forms.ModelChoiceField(queryset=InstrumentModels.objects.all().order_by('model'))
    owner = forms.ModelChoiceField(queryset=Customer.objects.all().order_by('site_name'))
    cal_due = forms.DateField(widget= forms.DateInput)
    location = forms.ModelChoiceField(queryset=Location.objects.all().order_by('instrument_location'))
    contam_status = forms.ModelChoiceField(queryset=ContamStatus.objects.all().order_by('contam_status'))
    notes = forms.CharField(widget = forms.Textarea, required = False)
    

    
    class Meta:
        model = Instrument
        exclude = ['instrument_id']
        # fields= "__all__"

# class RecieveSihpment(forms.ModelChoiceField):
#     def __init__(self, *args, **kwargs):
        
     
