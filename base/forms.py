from django import forms 
    
# creating a form  
class InputForm(forms.Form): 
    semester = forms.CharField(max_length=2)
    department = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=200)
    numberOfHours = forms.CharField(max_length=10)