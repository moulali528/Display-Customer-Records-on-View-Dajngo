from django import forms
from .models import CustomerRecords, CustomerDeletedRecords

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	postcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"postcode", "class":"form-control"}), label="")

	class Meta:
		model = CustomerRecords
		exclude = ("user",)

'''
# Create Deleted Record Form
class DeletedRecordForm(forms.ModelForm):
	first_name = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	postcode = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"postcode", "class":"form-control"}), label="")

	class Meta:
		model = CustomerDeletedRecords
		fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'postcode')
		#exclude = ("user",)

	#def clean(self):
    #		cleaned_data = super().clean()  # Don't forget to call super().clean()
        # Your custom cleaning logic
	#	return cleaned_data
		
'''