from django import forms
from .models import ClientQuestion

# precisa mostrar mensagem de erro quando o formulário não for válido e quando for válido mostrar mensagem de sucesso


class ClientQuestionForm(forms.ModelForm):
    client_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "", "placeholder": "Nome"}),
    )

    client_email = forms.EmailField(
        label="",
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "", "placeholder": "Email"}),
    )

    subject = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "", "placeholder": "Assunto"}),
    )

    message = forms.CharField(
        label="",
        max_length=100,
        widget=forms.Textarea(attrs={"class": "", "placeholder": "Mensagem"}),
    )

    class Meta:
        model = ClientQuestion
        fields = ["client_name", "client_email", "subject", "message"]

    def save(self, commit=True):
        client_question = super(ClientQuestionForm, self).save(commit=False)
        client_question.client_name = self.cleaned_data["client_name"]
        client_question.client_email = self.cleaned_data["client_email"]
        client_question.subject = self.cleaned_data["subject"]
        client_question.message = self.cleaned_data["message"]

        if commit:
            client_question.save()
        return client_question

    def clean_client_name(self):
        client_name = self.cleaned_data["client_name"]
        if not client_name:
            raise forms.ValidationError("O campo nome é obrigatório")
        return client_name

    def clean_client_email(self):
        client_email = self.cleaned_data["client_email"]
        if not client_email:
            raise forms.ValidationError("O campo email é obrigatório")
        return client_email

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if not subject:
            raise forms.ValidationError("O campo assunto é obrigatório")
        return subject

    def clean_message(self):
        message = self.cleaned_data["message"]
        if not message:
            raise forms.ValidationError("O campo mensagem é obrigatório")
        return message

    def clean(self):
        cleaned_data = super(ClientQuestionForm, self).clean()
        client_name = cleaned_data.get("client_name")
        client_email = cleaned_data.get("client_email")
        subject = cleaned_data.get("subject")
        message = cleaned_data.get("message")
        if not client_name and not client_email and not subject and not message:
            raise forms.ValidationError("Todos os campos são obrigatórios")
        return cleaned_data
