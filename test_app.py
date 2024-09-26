from app import app

Def test_hello_world():
   client=app.test_client()
   Response = client.get('/')
   Assert response.data==b'Hello, Jenkins!'