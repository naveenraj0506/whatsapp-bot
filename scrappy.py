from bs4 import BeautifulSoup
import urllib.request
import requests
import json

# def covid_tracker():
#     result = ""
#     fhandle = urllib.request.urlopen('https://www.mohfw.gov.in/')
#     data = fhandle.read().decode()
#     soup = BeautifulSoup(data, 'html.parser')
#     mydivs = soup.findAll("div", {"class": "iblock"})
#     for div in mydivs:
#         result = result+ div.text
#     return result

def ai_reply(myamsg):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ya29.c.Ko8BxQdHfRreb1XN5iOgDEizU41tjdIZur-2M0kapFOUTtCKzq4u5pn7Jw2kkargyj0M2VJUNGTQdumDnMnC3pLbfZA53vL2zZTM39luucmICXEz1KM0gpoBfbvgLrsdcIfpqYxKNfkpSe01AmkneRppl7UgYFCJPzwFsPi6EfMMko1upxr2e-hpn4cplEYphmw',
    }

    data = '{"queryInput":{"text":{"text":"'+myamsg+'","languageCode":"en"}},"queryParams":{"timeZone":"Asia/Calcutta"}}'

    response = requests.post(
        'https://dialogflow.googleapis.com/v2/projects/emma-ffynax/agent/sessions/0c863802-0296-0674-e00d-f34e020ee131:detectIntent',
        headers=headers, data=data)

    data = json.loads(response.text)

    return data['queryResult']['fulfillmentMessages'][0]['text']['text'][0]

