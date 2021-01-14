from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Member,Inventory,Booking
from django import forms
import re 
# class GuestAdminForm(forms.ModelForm):
#     def __init__(self,*args,**kwargs):
#         super(GuestAdminForm,self).__init__(*args,**kwargs)

#     def clean(self):
#         contact = self.cleaned_data.get('phone')
#         regex=r'^\d[10]$'
#         match=re.match(regex,contact)
#         if match is None:
#             raise forms.ValidationError('please enter a valid phone number', code='error')
#         return self.cleaned_data

#     def save(self,commit=True):
#         return super(GuestAdminForm,self).save(commit=commit)


class MemberAdmin(ImportExportModelAdmin):
    list_display = ('name','surname','date_joined','booking_count')
    # form = MemberAdminForm

admin.site.register(Member,MemberAdmin)

class InventoryAdmin(ImportExportModelAdmin):
    list_display=('id_no','title','description','remaining_count','expiration_date',)
    ordering = ['id_no']
    # form = InventoryAdminForm

admin.site.register(Inventory,InventoryAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display=('inventory','member','booking_date','is_active',)
    # form = BookingAdminForm

admin.site.register(Booking,BookingAdmin)

