import requests
API_KEY = "f9bcbd1a8d87805b30f591cbfd16612d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Introdu numele orasului: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    vreme = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]-213.15 , 2)
    vantul = data['wind']['speed']
    presiunea = data['main']['pressure']
    print("Vremea: ", vreme)
    print("Temperatura: ", temperature)
    print("Vantul: ", vantul)
    print("Presiunea: ", presiunea)
    f = open("file.txt", "w")
    f.write("presiunea: "+str(presiunea)+'/n'+("vantu: "))
else:
    print("Am o eroare")