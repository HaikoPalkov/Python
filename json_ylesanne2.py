import json
import requests

yl = "hindeline"
url = f"https://dummyjson.com/todos"
response = requests.get(url)

if response.status_code == 200:
    tehtud_ülesanne = 0
    todode_koguarv = 0
    data = response.json()
    for t in data["todos"]:
        print(t["todo"], t["completed"])
        todode_koguarv += 1
        if t["completed"]:
            tehtud_ülesanne += 1
    protsent = tehtud_ülesanne / todode_koguarv * 100
    print(f"tehtud_ülesanded: {tehtud_ülesanne}")
    print(f"todode arv: {todode_koguarv}")
    print("ülesannete protsent:", round(protsent, 2), "%")
else:
    print(response.status_code)






""" 7. Todos
 Kuva Ülesanded ja staatus (todo, completed) 
 Loenda tehtud ülesanded 
 Leia todode koguarv
 Arvuta tehtud ülesannete protsent  """