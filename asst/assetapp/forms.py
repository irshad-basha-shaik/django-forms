from django import forms


from django import forms



# creating a form
from .models import AssetModel

USAGE_TYPE = [
    ('Spare_Old', 'Spare_Old'),
    ('Spare_New', 'Spare_New')
]
LOCATION = [
    ('Hyd', 'Hyd'),
    ('Cht', 'Cht'),
    ('Kdp', 'Kdp'),
    ('Wg', 'Wg'),
    ('Eg', 'Eg'),
    ('Warangal', 'Warangal'),
]
MACHINE_TYPE = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
]
HDD = [
    ('120GB', '120GB'),
    ('240GB', '240GB'),
    ('500GB', '500GB'),
    ('1000GB', '1000GB'),
    ('2000GB', '2000GB'),
    ('10000GB', '10000GB'),
]
PROCESSOR = [
    ('Dual_Core','Dual_Core'),
    ('Core_I3_1st','Core_I3_1st'),
    ('Core_I3_2nd','Core_I3_2nd'),
    ('Core_I3_3rd','Core_I3_3rd'),
    ('Core_I3_4th','Core_I3_4th'),
    ('Core_I3_10th','Core_I3_10th'),
    ('Core_I5_1st','Core_I5_1st'),
    ('Core_I5_3rd','Core_I5_3rd'),
    ('Core_I5_10th','Core_I5_10th'),
    ('Core_I7_1st','Core_I7_1st'),
    ('Core_I7_3rd','Core_I7_3rd'),
    ('Core_I7_10th','Core_I7_10th')
]
YEARS= [x for x in range(1940,2021)]
class AssetForm(forms.ModelForm):
    '''location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    asset_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    emp_id = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    usage_type = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=USAGE_TYPE))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    gef_id_number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    domain_workgoup = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}))
    hdd_make = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd_model = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}))
    hdd_serial_no =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ram =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    processor_purchase_date = forms.DateField(label='Processor Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    processor = forms.ChoiceField(choices=PROCESSOR,widget=forms.Select(attrs={'class': 'form-control'}))
    '''
    class Meta:
        model = AssetModel
        fields = ['processor_purchase_date','processor']
