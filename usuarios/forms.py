from django import forms
from django.shortcuts import redirect



class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João Silva"
            }
        )
    )
    
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome Completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva",
            }
        )
    )  
    
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joãosilva@xpto.com",
            }
        )
    )  
    
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )
    
    confirm_senha=forms.CharField(
        label="Comfirmação de Senha",
        required=True,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Comfirme Senha",
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError("Espaços não são permitidos no campo nome")
            else:
                return nome
    
    def clean_confirm_senha(self):
        confirm_senha = self.cleaned_data.get("confirm_senha")
        senha = self.cleaned_data.get("senha")
        
        if senha and confirm_senha:
            if senha != confirm_senha:
                raise forms.ValidationError("Senhas não condizem")
            else:
                return confirm_senha

