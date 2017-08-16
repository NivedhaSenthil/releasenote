import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://gitlog.mingle.thoughtworks.com/api/v2/projects/%s/cards/%s.xml"


def get_card(project_name,card_no,user_name,password):
    url = BASE_URL %(project_name,card_no)
    return requests.get(url,auth=HTTPBasicAuth(user_name,password))


def get_cards_title(project_name,card_nos,user_name,password):
    card_details = []
    for card_no in card_nos:
        card_details.append(get_card(project_name,card_no,user_name,password))
    return card_details