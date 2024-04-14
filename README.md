# ProtestTools
#### A tool for organizing local community action
***
ProtestTools is a self-ran instanced community organizing tool. 
The core tenets that were in mind while designing ProtestTools were:
1. Most minimal user data stored as possible
2. Entirely self-hosted
3. Simple and useful functionality to organize meetings or events
### Technologies Used:
- [Flask](https://github.com/pallets/flask/) (with [flask_login](https://github.com/maxcountryman/flask-login))
- [MongoDB Atlas](https://www.mongodb.com/atlas/database) (using [PyMongo](https://github.com/mongodb/mongo-python-driver))
- [folium](https://github.com/python-visualization/folium)
- [Leaflet.js](https://github.com/Leaflet/Leaflet)

# Example Pictures
## Home Page
![An image of homepage of ProtestTools. The image shows a column on the left side listing events,
with the right side being dominated by a map filled with various points](screenshots/event_view.png)
The home page lists the various events contained in the instance of ProtestTools.
Each button on the bottom right of the cards will take you to that events respective event page.

## Generate Invites
![An image of the generate invite screen. It has ProtestTools in large type on the left.
On the right is an entry box for the amount of invite uses, 
as well as a large button undernearth it](screenshots/generate_invite.png)
Users are able to generate invite links, which can allow new members to access that instance of ProtestTools.   
---
