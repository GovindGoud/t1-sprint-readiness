import requests

print("Lab 7: Integration Task")
print("Combining Python Script + API + Git")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        data = response.json()
        print("\nAPI Call Successful")
        print("Post ID:", data["id"])
        print("Title:", data["title"])
    else:
        print("API failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("API Error:", e)
