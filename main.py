import  requests

response = requests.get("https://www.google.com")

with open('index.html', 'w') as f :
    f.write(response.text)


