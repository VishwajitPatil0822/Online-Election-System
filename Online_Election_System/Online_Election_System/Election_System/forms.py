from django import forms
from .models import Newregistration,Voterregistration,Completedvote,Result

class NewregistrationForm(forms.ModelForm):
    class Meta:
        model = Newregistration
        fields = '__all__'

        labels = {
            'fullname' : 'Enter Your Full Name :',
            'dob' : 'Enter Your Date Of Birth :',
            'sex' : 'Enter Your Gender :',
            'city' : 'Enter Your City :',
            'taluka' : 'Enter Your Taluka :',
            'dist' : 'Enter Your Dist :',
            'state': 'Enter Your State :',
            'pincode': 'Enter Your Pin Code :',
            'addharno': 'Enter Your Addhar No :',
            'voterid': 'Enter Your Voter Id :',
            'mobno': 'Enter Your Mobile No :',
            'email': 'Enter Your Email :'
        }

        widgets = {
            'dob': forms.DateInput(attrs={'type':'date'})
        }

class VoterregistrationForm(forms.ModelForm):
    class Meta:
        model = Voterregistration
        fields = '__all__'

        labels = {
            'fullname' : 'Enter Your Full Name :',
            'dob' : 'Enter Your Date Of Birth :',
            'sex' : 'Enter Your Gender :',
            'city' : 'Enter Your City :',
            'taluka' : 'Enter Your Taluka :',
            'dist' : 'Enter Your Dist :',
            'state': 'Enter Your State :',
            'pincode': 'Enter Your Pin Code :',
            'addharno': 'Enter Your Addhar No :',
            'voterid': 'Enter Your Voter Id :',
            'mobno': 'Enter Your Mobile No :',
            'email': 'Enter Your Email :',
            'partynm': 'Enter Your Party Name :',
            'partyimg': 'Enter Your Party Logo :'
        }

        widgets = {
            'dob': forms.DateInput(attrs={'type':'date'})
        }

class VoteForm(forms.ModelForm):
    class Meta:
        model = Completedvote
#        fields = '__all__'
        fields = ['voterid', 'fullname']

        labels = {
            'voterid': 'Enter Your Voter Id :',
            'fullname': 'Enter Your Full Name :'
        }

