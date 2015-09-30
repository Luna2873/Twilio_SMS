from django import forms
 
class Msg(forms.Form):
    
    phone = forms.CharField(
    	label = 'Send to', 
    	widget=forms.TextInput(attrs={'placeholder': 'Phone#'}))
    msg = forms.CharField(
    	
    	label='Content', 
    	max_length=160, 
    	widget=forms.Textarea, 
    	help_text='160 characters max.')