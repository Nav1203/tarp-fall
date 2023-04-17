import pyrebase
config={
    "apiKey": "AIzaSyDJgcH85qBoOOwUxY-WsWtQFWiZwWWcaVs",
  "authDomain": "fall-det.firebaseapp.com",
  "projectId": "fall-det",
  "databaseURL": "https://fall-det-default-rtdb.firebaseio.com",
  "storageBucket": "fall-det.appspot.com",
  "messagingSenderId": "508646580821",
  "appId": "1:508646580821:web:1531df570385646532aadc"
}
fb=pyrebase.initialize_app(config)
stg=fb.storage()
print(stg.child("images/img1.jpg").get_url(token=None))