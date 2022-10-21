from django.forms import ModelForm
from .models import Sister, Chapter


# class SisterForm(ModelForm):
#     class Meta:
#         model = Sister
#         fields = ['first_name', 'last_name', 'nickname', 'chapter', 'nickname', 'crossing_chapter', 'crossing_semester',
#                   'big_sister', 'little_sister_crossed', 'tree', 'line_number', 'status']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['chapter'].queryset = Chapter.objects.all()

# little_sister_process = models.ManyToManyField(PNM, null=True)
