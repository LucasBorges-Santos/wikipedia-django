from django.shortcuts import render
from .pesquisa import pesquisa
from .form import PesquisaForm
import wikipedia


# Create your views here.


def index(request):
    form = PesquisaForm(request.GET)

    context = {
        'form': form
    }

    if form.is_valid():
        chave = form.cleaned_data['pesquisa']

        try:
            resultado = pesquisa(chave)

            context['titulo'] = resultado.title
            context['resumo'] = resultado.summary.split('\n')
            context['url'] = resultado.url

        except wikipedia.DisambiguationError as e:
            context['opcoes'] = e.options

        except wikipedia.PageError as e:
            context['mensagem'] = 'Dados de pesquisa não encontrado, tente novamente.'

        return render(request, 'BuscaWikipedia/index.html', context=context)

    else:
        context['mensagem'] = 'Informe um dado para pesquisa.'
        return render(request, 'BuscaWikipedia/index.html', context=context)
