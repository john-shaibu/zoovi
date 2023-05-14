from dataclasses import field
from django.forms import ModelForm, FileInput
from .models import Video


class uploadForm(ModelForm):
      class Meta:
            model = Video
            fields = ('video',)
            widgets = {
                  'video': FileInput(attrs={'class': 'file-input', 'accept': '.mp4', 'hidden': 'True'}),
            }