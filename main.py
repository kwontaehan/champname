
import requests
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
url='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/champion/Aatrox.json'
res = requests.get(url).json()

champ_lst = (res['data']['Aatrox']['key'],res['data']['Aatrox']['name'])