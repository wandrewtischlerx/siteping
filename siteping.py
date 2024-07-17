import os
from http.client import HTTPConnection, HTTPSConnection
from colorama import Fore, Style, init



print("   _____   _   _            _____    _                 ")
print("  / ____| (_) | |          |  __ \  (_)                ")
print(" | (___    _  | |_    ___  | |__) |  _   _ __     __ _ ")
print("  \___ \  | | | __|  / _ \ |  ___/  | | | '_ \   / _` |")
print("  ____) | | | | |_  |  __/ | |      | | | | | | | (_| |")
print(" |_____/  |_|  \__|  \___| |_|      |_| |_| |_|  \__, |")
print("                                                  __/ |")
print("    Desenvolvido Por @WandrewTischler   V0.1     |___/ \n")







# Inicializa o colorama
init(autoreset=True)

# Caminho absoluto do arquivo de entrada e saída
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, 'sites.txt')
output_file = os.path.join(current_dir, 'sites_online.txt')

# Dicionário de status HTTP
http_statuses = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported"
}

# Função para verificar se o site está online usando http.client
def check_site(url):
    def get_response(url, use_https=True):
        try:
            conn = HTTPSConnection(url, timeout=5) if use_https else HTTPConnection(url, timeout=5)
            conn.request("HEAD", "/")
            return conn.getresponse()
        except Exception:
            return None

    response = get_response(url)
    if not response:
        response = get_response(url, use_https=False)
    
    if response:
        return response.status, http_statuses.get(response.status, "Unknown Status")
    else:
        return None, "Sem resposta"

# Lista para armazenar os sites online e com erro de servidor
online_sites = []
error_sites = []

# Ler o arquivo de entrada
with open(input_file, 'r') as file:
    sites = file.readlines()

# Verificar cada site
for site in sites:
    site = site.strip()
    status, status_message = check_site(site)
    if status:
        if status == 200:
            print(Fore.GREEN + f"{site} está online ({status} {status_message})")
            online_sites.append(f"{site} ({status} {status_message})")
        elif status == 500:
            print(Fore.YELLOW + f"{site} não está online ({status} {status_message})")
            error_sites.append(f"{site} ({status} {status_message})")
        else:
            print(Fore.RED + f"{site} não está online ({status} {status_message})")
    else:
        print(Fore.RED + f"{site} não está online ({status_message})")

# Escrever os sites online no arquivo de saída
with open(output_file, 'w') as file:
    for site in online_sites:
        file.write(site + '\n')

# Imprimir sites com status 200 e 500
print(Fore.BLUE + "\nSites online (200 OK):")
for site in online_sites:
    print(site)

print(Fore.BLUE + "\nSites com erro de servidor (500 Internal Server Error):")
for site in error_sites:
    print(site)

# Imprimir contagem total
print(Fore.BLUE + f"\nTotal de sites online (200 OK): {len(online_sites)}")
print(Fore.BLUE + f"Total de sites com erro de servidor (500 Internal Server Error): {len(error_sites)}")

print(Fore.BLUE + f"\nSites online salvos em {output_file}")
