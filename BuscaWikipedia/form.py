from django import forms


class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(label='Pesquise', max_length=20)