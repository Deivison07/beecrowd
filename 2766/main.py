import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

valor_em_dolar_formatado = locale.currency(123456, grouping=True)
print(valor_em_dolar_formatado)