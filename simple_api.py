import requests
from bs4 import BeautifulSoup

def get_weather(city):
    city_query = city.replace(' ', '+')
    url = f"https://weather.com/weather/today/l/{city_query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Could not retrieve weather for {city}.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    temp = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ')
    condition = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr')

    temperature = temp.text if temp else "N/A"
    weather = condition.text if condition else "N/A"

    if "rain" in weather.lower():
        status = "Rainy"
    elif "sun" in weather.lower() or "clear" in weather.lower():
        status = "Sunny"
    else:
        status = weather

    print(f"Weather in {city.title()}: {temperature}, {status}")

## if __name__ == "__main__":
    print("Fetching weather for Boston...")
    get_weather("Boston")

    city = input("Enter another city: ")
    get_weather(city)