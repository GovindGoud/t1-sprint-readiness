import requests

print("Mini Sprint Challenge")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        data = response.json()
        print("Title:", data["title"])
    else:
        print("API failed")

except Exception as e:
    print("Error:", e)
