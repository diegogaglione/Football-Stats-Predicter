import requests
from bs4 import BeautifulSoup
squadre = {}
ids = ['stats_squads_standard_for', 'stats_squads_standard_against', 'stats_squads_keeper_for', 'stats_squads_keeper_against', 'stats_squads_keeper_adv_for', 'stats_squads_keeper_adv_against', 'stats_squads_shooting_for', 'stats_squads_shooting_against', 'stats_squads_passing_for', 'stats_squads_passing_against', 'stats_squads_passing_types_for', 'stats_squads_passing_types_against', 'stats_squads_gca_for', 'stats_squads_gca_against', 'stats_squads_defense_for', 'stats_squads_defense_against', 'stats_squads_possession_for', 'stats_squads_possession_against', 'stats_squads_playing_time_for', 'stats_squads_playing_time_against', 'stats_squads_misc_for', 'stats_squads_misc_against']
def ottieni_pagina():
            page = "https://fbref.com/en/comps/11/Serie-A-Stats"
            html_content = requests.get(page).text
            soup = BeautifulSoup(html_content, "html.parser")
            for id in ids:
                table = soup.find("table", {"id": id})
                body = table.find("tbody").find_all("tr")
                for row in body:
                    th = row.find("th")
                    nome = th.find("a", href=True)
                    nome = nome.text
                    if nome not in squadre:
                        squadre[nome] = {}
                    th = row.findAll("td")
                    for x in th:
                        if x.get("data-stat") not in squadre[nome]:    
                            squadre[nome][x.get("data-stat")] = x.text
            print(squadre["Atalanta"])

ottieni_pagina()

