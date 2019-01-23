#who is in space
import json
import turtle
import urllib.request
url='http://api.open-notify.org/astros.json'
response=urllib.request.urlopen(url)
result=json.loads(response.read())
print('People in space:',result['number'])
people=result['people']
for p in people:
    print(p['name'],'in',p['craft'])
#now where is the space station
url2='http://api.open-notify.org/iss-now.json'
response2=urllib.request.urlopen(url2)
result2=json.loads(response2.read())
location=result2['iss_position']
lat=location['latitude']
lon=location['longitude']
print('latitude:',lat)
print('longitude:',lon)
screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')
screen.register_shape('iss.gif')
iss=turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
#go to current location
iss.penup()
iss.goto(float(lon),float(lat))
turtle.done()








