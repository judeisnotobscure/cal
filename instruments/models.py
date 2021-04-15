from django.db import models

# Create your models here.
from django.db import models
from .extended_models import IntegerRangeField
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from autoslug import AutoSlugField

##############################
## Primary Models   ###########
##############################
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, editable=False)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    site_name = models.CharField(max_length=64, blank=True, null=True)
    

    def __str__(self):
        return "{}: {}".format(self.site_name, self.company_name)

    class Meta:
        managed = True
        db_table = 'customer'


class InstrumentType(models.Model):
    """This model is to list the types such as dose rate meter, extending, area, frisker"""
    instrument_type_id = models.AutoField(primary_key = True, editable = False)
    instrument_types = models.CharField(max_length=64,  blank=True, null=True)

    def __str__(self):
        return self.instrument_types

    class Meta:
        managed = True
        db_table = 'instrument_uses'

class Location(models.Model):
    """This model lists the instrument location types such as cal facility, home site"""
    location_id= models.AutoField(primary_key = True, editable = False)
    instrument_location = models.CharField(max_length = 64,blank=True, null=True)

    def __str__(self):
        return self.instrument_location

    class Meta:
        managed = True
        db_table = 'instrument_location'

class Status(models.Model):
    """This model lists the instrument status types such as recieved, processed, shipped"""
    status_id= models.AutoField(primary_key = True, editable = False)
    instrument_status = models.CharField(max_length = 64,blank=True, null=True)

    def __str__(self):
        return self.instrument_status

    class Meta:
        managed = True
        db_table = 'instrument_status'

class ContamStatus(models.Model):
    """This model holds values for insturment contamination status, yes or no"""
    contam_id =models.AutoField(primary_key = True, editable = False)
    contam_status = models.CharField(max_length = 64,blank=True, null=True)

    def __str__(self):
        return self.contam_status

    class Meta:
        managed = True
        db_table = 'contam_status'
##############################
##  Dependent Models   ###########
##############################
class InstrumentModels(models.Model):
    manufacturer = models.CharField(max_length=48)
    model = models.CharField(max_length=48)
    instrument_type= models.ForeignKey('InstrumentType',models.DO_NOTHING, db_column='instrument_type', blank=True, null=True)
    def __str__(self):
        return self.model
    

    class Meta:
        managed = True
        db_table = 'instrument_models'

##############################
##  2nd layer Dependent Models   ###########
##############################
class Instrument(models.Model):
    #primary info
    instrument_id = models.AutoField(primary_key=True, editable=False)
    serial_number = models.CharField(max_length=24)
    instrument_model = models.ForeignKey('InstrumentModels', models.DO_NOTHING, db_column= "instrument_model",blank=True, null=True)
    owner = models.ForeignKey('Customer', models.DO_NOTHING, db_column= "owner", blank=True, null=True)
    # info that changes
    cal_due = models.DateField(auto_now=False, db_column = 'cal_due')
    notes = models.CharField(db_column = 'notes', max_length=512, blank= True, null = True)
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='location', blank= True, null = True)
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status', blank= True, null = True)
    contam_status = models.ForeignKey('ContamStatus', models.DO_NOTHING, db_column= "contam_status",blank=True, null=True)
    #  ### Slug field may be needed for selecting in single object view
    slug = AutoSlugField(null=True, default=None, unique= True, populate_from= 'serial_number',max_length = 200)

    def __str__(self):
        # if self.cal_due >
        return "{} {}".format(self.serial_number, self.instrument_model)
    
    
        
    class Meta:
        managed = True
        db_table = 'instruments'