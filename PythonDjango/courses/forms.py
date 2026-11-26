from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'seats']

    def clean_seats(self):
        seats = self.cleaned_data.get('seats')
        if seats is None or seats < 1 or seats > 30:
            raise forms.ValidationError("Мест должно быть от 1 до 30.")
        return seats