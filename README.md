<img src="https://raw.githubusercontent.com/wandrewtischlerx/siteping/main/siteping.PNG" alt="Print SitePing">

<h1>SitePing</h1>

---

Bem-vindo ao SitePing, uma ferramenta eficiente e fácil de usar desenvolvida para profissionais de rede e desenvolvedores focados em monitorar a disponibilidade de sites.

Funções Principais

- Verificar Disponibilidade de Sites: Verifica se os sites estão online.
- Relatório de Status: Gera um relatório com os status HTTP dos sites verificados.
- Destaque para Erros de Servidor: Colore em amarelo os sites que retornam "Internal Server Error" (500).

<h2>Instalação:</h2>

```
git clone github.com/wandrewtischlerx/siteping
cd siteping
pip install -r requirements.txt
```


<h2>Uso</h2>

1. Adicione os URLs dos sites que deseja verificar no arquivo `sites.txt`.
2. Execute o script:

```
python siteping.py
```

3. O script irá verificar cada site listado e gerar um relatório com os seguintes detalhes:
   - Sites online (status 200)
   - Sites com erro de servidor (status 500)
   - Outros status HTTP

<h2>Contribuições:</h2>

Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, por favor abra uma issue ou envie um pull request.

<h2>Licença:</h2>

Este projeto está licenciado sob a MIT License (https://opensource.org/licenses/MIT).

---

Utilize o SitePing para monitorar e assegurar a disponibilidade dos seus sites de forma simples e eficaz!

Desenvolvido por Wandrew Tischler
