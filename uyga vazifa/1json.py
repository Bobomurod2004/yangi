# from http.client import responses
# from itertools import count
# from http.client import responses
from tkinter.font import names

# requests=requests.get("https://admin.soffstudy.uz/api/v1/gallery/?limit=9&offset=9")
#
# a=requests.json().get("data")
# # print(requests.json().get("data"))
# # print(requests.)
#
# for result in a:
#     print(result.get("name"))
# print(requests.json().get("count"))
# print(count)

#



# import requests
# class Websoff:
#     def __init__(self, url):
#         self.url = url
#
#     @staticmethod
#     def get_json_data(url):
#         response = requests.get(url)
#         return response.json().get("data")
#
#     def get_data(self):
#         response = self.get_json_data(self.url)
#         return response
#
#     for result in get_json_data("https://admin.soffstudy.uz/api/v1/gallery/?limit=9&offset=0"):
#         name = result.get("name")
#         print(result.get("name"))
#
#     @staticmethod
#     def telegram_yuborish(token,chat_id,text):
#         url = f"https://api.telegram.org/bot{token}/sendMessage"
#         response = requests.post(url=url, data={"chat_id": chat_id, "text": text})
#         if response.status_code ==200:
#             print("xabar muvofaqatli")
#         else:
#             print("error")
#
# token = "7639005796:AAHU6moXHX_VtoR9AO-4WSAiqU12z0IDNiw"
# chat_id = 5652442685


# url = "https://admin.soffstudy.uz/api/v1/gallery/?limit=9&offset=0"
# web = Websoff(url = url)
# x=web.get_data()
# print(x)


import requests

class Websoff:
    def __init__(self, url):
        self.url = url

    @staticmethod
    def get_json_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # HTTP xatolarni aniqlash
            data = response.json().get("data")  # API'dan "data" kalitini olish
            if isinstance(data, list):  # Faqat ro‘yxat bo‘lsa qaytariladi
                return data
            print("Xato: 'data' ro‘yxat emas yoki bo‘sh.")
            return []
        except requests.exceptions.RequestException as e:
            print(f"Xatolik: {e}")
            return []

    def get_data(self):
        return Websoff.get_json_data(self.url)


# Telegramga xabar yuborish funksiyasi
def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        response = requests.post(url, data={"chat_id": chat_id, "text": text})
        response.raise_for_status()  # HTTP xatolarni aniqlash
        print(f"Xabar yuborildi: {text}")
    except requests.exceptions.RequestException as e:
        print(f"Telegram API xatosi: {e}")


# API URL va ma'lumot olish
url = "https://admin.soffstudy.uz/api/v1/gallery/?limit=9&offset=0"
web = Websoff(url)
data = web.get_data()  # API'dan "data" qismini olish

# Telegram bot uchun token va chat ID
token = "7639005796:AAHU6moXHX_VtoR9AO-4WSAiqU12z0IDNiw"
chat_id = 5652442685

# "name" maydonidagi barcha qiymatlarni Telegramga yuborish
if data:  # Ma'lumot bo‘lsa
    for result in data:
        name = result.get("name")
        if name:  # Agar "name" mavjud bo‘lsa
            send_telegram_message(token, chat_id, name)
else:
    print("API'dan hech qanday ma'lumot olinmadi.")

