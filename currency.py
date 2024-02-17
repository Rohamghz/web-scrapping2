import requests
import bs4

req = requests.get("https://www.tgju.org/profile/price_eur")
text = req.text

soup = bs4.BeautifulSoup(text, "html.parser")
a = soup.find_all("span", attrs={"data-col":"info.last_trade.PDrCotVal"})

l = []

for i in a:
    l.append(i.text)

print(f"1 EUR = {l[0]} IRR")
########################################################

req_1 = requests.get("https://www.tgju.org/profile/price_dollar_rl")
text_1 = req_1.text

soup_1 = bs4.BeautifulSoup(text_1, "html.parser")
a_1 = soup_1.find_all("span", attrs={"data-col":"info.last_trade.PDrCotVal"})

j =[]

for i in a_1:
    j.append(i.text)

print(f"1 USD = {j[0]} IRR")