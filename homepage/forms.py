from django import forms


class NewsletterForm(forms.Form):
    '''
    Form for sending newsletter
    '''
    subject = forms.CharField(max_length=120)
    recipients = forms.CharField()
    message_body = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        placeholders = {
            'subject': 'Subject',
            'recipients': 'Recipients',
            'message_body': 'Message',
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
