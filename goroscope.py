import requests
from datetime import date



def find(text: str) -> str:
    today = date.today().strftime("%d.%m.%Y")
    text = f'Придумай гороскоп на сегодня для человека, который родился {text}. Сегодня - {today}.'
    url = f"https://text.pollinations.ai/{text}"
    r = requests.get(url)
    return r.text

