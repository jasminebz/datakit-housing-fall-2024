import requests
from bs4 import BeautifulSoup

def get_edm_neighbourhoods():
    url = "https://www.edmonton.ca/residential_neighbourhoods/neighbourhoods/neighbourhood-profiles"

    soup = BeautifulSoup(requests.get(url), "html.parser")

    all_neighbourhoods = soup.find(class_= "row block-content__content")

    for n in all_neighbourhoods.find_all("p"):
        return n.text
