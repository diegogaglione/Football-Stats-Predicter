import requests
from bs4 import BeautifulSoup

class fsp_main:
    def __init__(self):
        self.squadre = {}
        self.soup = None
        self.table = None
        self.no_name_dupe = True

    def ottieni_pagina(self):
        page = "https://fbref.com/en/comps/11/Serie-A-Stats"
        html_content = requests.get(page).text
        soup = BeautifulSoup(html_content, "html.parser")
        self.table = soup.find_all("table")[2:]

    def ottieni_nome_squadra(self):
        for y in self.table:
            body = y.find("tbody").find_all("tr")
            for row in body:
                if self.no_name_dupe is True:
                    th = row.find("th")
                    nome = th.find("a", href=True)
                    nome = nome.text
                    self.squadre[nome] = {}
                th = row.findAll("td")
                for x in th:
                    self.squadre[nome][x.get("data-stat")] = x.text
            self.no_name_dupe = False
fsp = fsp_main()
fsp.ottieni_pagina()
fsp.ottieni_nome_squadra()

