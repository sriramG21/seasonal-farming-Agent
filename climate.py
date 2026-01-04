import requests as re

def curr_weather(city,api_key):
    url=("https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric")
    response=re.get(url)
    data=response.json()
    return{
        "Temperature":data["main"]["temp"],
        "Condition":data["weather"][0]["main"],
        "Rainfall":data.get("rain", {}).get("1h", 0)
    }


