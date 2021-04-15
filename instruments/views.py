from django.shortcuts import render, redirect
from .filters import InstrumentFilter
from .models import Instrument, InstrumentModels, Customer
from django.views.generic import View, TemplateView, DetailView
from django.views.generic.edit import UpdateView
import datetime
from django.utils import timezone
from django.http import HttpResponse
from . import forms


######################
#### Main page Search
#######################
def search(request):
    instrument_list = Instrument.objects.all()
    instrument_filter = InstrumentFilter(request.GET, queryset= instrument_list)
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,'instruments/search.html', {'filter': instrument_filter})


######################
#### Add Instrument Page
#######################
def form_name_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    form = forms.AddInstrument()
    if request.method == 'POST':
        form = forms.AddInstrument(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # do something
            print("validation success")
            print("Serial: "+form.cleaned_data['serial_number'])
            print("Model: "+str(form.cleaned_data['instrument_model']))
            print("Text: "+form.cleaned_data['notes'])
        else:
            print("Error: Invalid From")
    return render(request, 'instruments/view_record.html', {'form':form})

######################
#### Detail View
#######################
class InstrumentDetailView(UpdateView):
    model = Instrument
    context_object_name = "instrument"
    template_name = 'intstruments/update_detail.html'
    fields = [
        'cal_due',
        'status',
        'location',
        'notes'

    ]

    success_url = '/'

######################
#### Recieve Shipment
#######################
def recieve_shipment(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    instrument_list = Instrument.objects.all()
    instrument_filter = InstrumentFilter(request.GET, queryset= instrument_list)
    return render(request,'instruments/recieve/recieve_shipment.html', {'filter': instrument_filter})


######################
#### Recieve Detail View
#######################
class InstrumentDetailView(UpdateView):
    ### Empty List 
    i_list = []
    

    model = Instrument
    context_object_name = "instrument"
    template_name = 'instruments/recieve/recieve_single.html'
    fields = [
        'status',
        'location',
        'cal_due',
        'notes'

    ]

    success_url = '/recieve'

