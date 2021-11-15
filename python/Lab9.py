import requests
import json
    
r = requests.get('http://localhost:3000')
aList = r.json()

r.json = [{"name":"widget1","color":"blue"},{"name":"widget2","color":"green"},{"name":"widget3","color":"black"},{"name":"widgetX","color":"blue"}]
aList = json.loads()
<<<<<<< HEAD
print("The color and name of the widget is " (aList['name'][0]['color']))
=======
print("The color and name of the widget is " (aList['name'][0]['color']))
>>>>>>> 139bcec2693d17ce40a4c43c6af4bdc693b044ca
