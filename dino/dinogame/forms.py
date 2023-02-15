from django import forms

from dinogame.models import Participant

#Forms for the missing person db
class ParticipantCreateForm(forms.ModelForm):
    class Meta:
        model = Participant
        # fields = "__all__"
        exclude = ['created_date', ]