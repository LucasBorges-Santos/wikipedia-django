import wikipedia


def pesquisa(chave):
    chave = str(chave)
    wikipedia.set_lang('pt')
    return wikipedia.page(chave)