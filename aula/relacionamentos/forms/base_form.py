from django.forms import ModelForm

class Baseform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.visible_fields():
            campo.field.widget.attrs.update({"class": "form-control"})
            if len(campo.errors.data) > 0:
                campo.field.widget.attrs.update({"class": "form-control is_invalid"})