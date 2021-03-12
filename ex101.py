from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, o voto não é obrigatorio.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcional.'
    else:
        return f'com {idade} anos, o voto é obrigario.'


print(voto(int(input('Ano de nascimento:'))))