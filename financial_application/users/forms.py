from .models import Account, Bank, Customer, CardInfo
from django import forms



class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_num', 'account_name', 'account_type', 'account_bal', 'customer_id', 'bank_name']


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name', 'routing_number', 'bank_phone']

class UserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'last_name', 'first_name', 'phone_number', 'email']

class CardForm(forms.ModelForm):
    class Meta:
        model = CardInfo
        fields = ['card_number', 'card_holder', 'card_issuer', 'security_code', 'expiration', 'customer_id', 'last_four_digits']
