import requests
from cfg import token, group_id


def send(url, amount, coupon):
    r = requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={group_id}&text=Плейлист: {url}\nКоличество: {amount}\nКупон: {coupon}'
    )
    return str(r.status_code)