"""Companies forms."""

# Django
from django import forms

# Models
from CarService.apps.admin_website.models.bank_accounts import BankAccounts
from CarService.apps.admin_website.models.cities import Cities
from CarService.apps.admin_website.models.companies import Companies

COMPANY_STATE_CHOICES = [
    ('Activa', 'Activa'),
    ('Inactiva', 'Inactiva'),
]


class CompanyForm(forms.Form):
    """Profile form."""

    city_name = forms.CharField(max_length=128, required=True)
    bank_account_cbu = forms.CharField(max_length=255, required=True)
    bank_account_name = forms.CharField(max_length=128, required=True)
    cuit = forms.CharField(max_length=11, required=True)
    business_name = forms.CharField(max_length=128, required=True)
    contact_person = forms.CharField(max_length=128, required=False)
    phone = forms.CharField(max_length=20, required=False)
    mobile = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=254, required=True)
    address_number = forms.IntegerField(required=True)
    email = forms.CharField(max_length=200, required=False)
    website = forms.URLField(max_length=200, required=False)
    details = forms.CharField(max_length=255, required=False)
    state = forms.CharField(max_length=64, required=True)


class CreateCompanyForm(forms.Form):
    """Create Company form."""
    localidad = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label="Selecciona una provincia")
    banco = forms.CharField(max_length=128, required=True)
    banco_cbu = forms.CharField(max_length=255, required=True)
    cuit = forms.CharField(max_length=11, required=True)
    razon_social = forms.CharField(max_length=128, required=True)
    persona_de_contacto = forms.CharField(max_length=128, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    celular = forms.CharField(max_length=20, required=False)
    direccion = forms.CharField(max_length=254, required=True)
    numero = forms.IntegerField(required=True)
    correo_electronico = forms.CharField(max_length=200, required=False)
    sitio_web = forms.URLField(max_length=200, required=False)
    detalles = forms.CharField(max_length=255, required=False)
    estado = forms.ChoiceField(choices=COMPANY_STATE_CHOICES)

    def clean_cuit(self):
        """CUIT must be unique."""
        cuit = self.cleaned_data['cuit']
        cuit_taken = Companies.objects.filter(cuit=cuit).exists()
        if cuit_taken:
            raise forms.ValidationError('CUIT en uso!')
        return cuit

    def save(self):
        """Create company and bank account."""
        data = self.cleaned_data

        bankaccount = BankAccounts.objects.create(
            cbu=data['banco_cbu'],
            bank=data['banco'],
        )
        bankaccount.save()
        loc_city = Cities.objects.get(name=data['localidad'])
        company = Companies.objects.create(
            city = loc_city,
            bank_account = bankaccount,
            cuit = data['cuit'],
            business_name = data['razon_social'],
            contact_person = data['persona_de_contacto'],
            phone = data['telefono'],
            mobile = data['celular'],
            address = data['direccion'],
            address_number = data['numero'],
            email = data['correo_electronico'],
            website = data['sitio_web'],
            details = data['detalles'],
            company_type = 'Aseguradora',
            state = data['estado'],
        )
        company.save()
