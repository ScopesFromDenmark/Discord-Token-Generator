import requests
import json
import time

discordname = input('Discord Account Name: ')
DiscordEmail = input('Email (You can just put random shit):')
Invitecode = input('Server invite Only Code Not Link (Fx 9282zx): ')
CapchaKey = input('Your Recapcha Key: ')



url = "https://discord.com/api/v9/auth/register"

payload = json.dumps({
  "fingerprint": "868288326208200704.pVrX2etGrXDtW4tpy0mYQIKQKMg",
  "email": DiscordEmail,
  "username": discordname,
  "password": "Bloit99",
  "invite": Invitecode,
  "consent": True,
  "date_of_birth": "1991-04-05",
  "gift_code_sku_id": None,
  "captcha_key": CapchaKey #API KEY!!!!!
})
headers = {
  'authority': 'discord.com',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRhLURLIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMDcgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjkyLjAuNDUxNS4xMDciLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LnlvdXR1YmUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cueW91dHViZS5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTEwNjAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
  'x-fingerprint': '868288326208200704.pVrX2etGrXDtW4tpy0mYQIKQKMg',
  'accept-language': 'da',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
  'content-type': 'application/json',
  'accept': '*/*',
  'origin': 'https://discord.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://discord.com/register',
  'cookie': '__dcfduid=68f23691ee9d14c8046ce0e1b62db35c; locale=da; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jul+24+2021+02%3A27%3A37+GMT%2B0200+(Centraleurop%C3%A6isk+sommertid)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0'
}


while True:
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(3)
