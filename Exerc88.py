import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print("O site não está acessível.")
else:
    print(f"O site está acessivel!")
