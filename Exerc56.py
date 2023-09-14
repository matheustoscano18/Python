times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminense',
         'Cruzeiro', 'Grêmio', 'São Paulo', 'Vasco', 'Atlético-MG', 'Santos',
         'Bragantino', 'Flamengo', 'Athletico-PR', 'Bahia', 'Goiás', 'Corinthians',
         'Cuiabá', 'Coritiba', 'América-MG')
print(f"Lista de times do brasileirão: {times}")
print("-=" * 15)
print(f"Os primeiros 5 são: {times[:5]}")
print("-=" * 15)
print(f"Os últimos 4 são: {times[-4:]}")
print("-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 15)
print(f"O Palmeiras está na {times.index('Palmeiras') + 1}º Posição")
