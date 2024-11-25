import requests
from bs4 import BeautifulSoup

class fsp_main:
    def __init__(self):
        self.squadre = {}
        self.soup = None
        self.table = None

    def ottieni_pagina(self):
        page = "https://fbref.com/en/comps/11/Serie-A-Stats"
        html_content = requests.get(page).text
        soup = BeautifulSoup(html_content, "html.parser")
        self.table = soup.find("table", {"id": "stats_squads_shooting_for"})

    def ottieni_nome_squadra(self):
        body = self.table.find("tbody").find_all("tr")
        for row in body:
            th = row.find("th")
            nome = th.find("a", href=True)
            nome = nome.text
            self.squadre[nome] = {}
            th = row.findAll("td")
            for x in th:
                self.squadre[nome][x.get("data-stat")] = x.text
fsp = fsp_main()
fsp.ottieni_pagina()
fsp.ottieni_nome_squadra()

