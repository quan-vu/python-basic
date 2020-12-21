import os
import requests
import json

AUTH_FILE='auth_key.txt'


class Auth:
  def __init__(self, email, password, login_url):
    self.email = email
    self.password = password
    self.login_url = login_url
    self.payload = {
      "email": email, 
      "password": password
    }
    self.headers = {
      'Content-Type': 'application/json'
    }
    self._initAuth()

  def _initAuth(self):
    if os.path.isfile(AUTH_FILE):
      print ("Initialed: {0}".format(AUTH_FILE))
    else:
      print("Init {0}".format(AUTH_FILE))
      self._saveAuthFile(access_token="")

  def _login(self):
    try:
      response = requests.request("POST", self.login_url, headers=self.headers, data=json.dumps(self.payload))
      response.raise_for_status()
      data = response.json()
      access_token = data['data']['token']
      # Save access token for next times
      self._saveAuthFile(access_token)
      print("Login success.")      
      return access_token
    except requests.exceptions.HTTPError as errh:
      print(errh)
    except requests.exceptions.ConnectionError as errc:
      print(errc)
    except requests.exceptions.Timeout as errt:
      print(errt)
    except requests.exceptions.RequestException as err:
      print(err)

  def _saveAuthFile(self, access_token):
    data = {
      "access_token": access_token
    }
    with open(AUTH_FILE, 'w') as outfile:
      json.dump(data, outfile)

  def getAccessToken(self):
    with open(AUTH_FILE) as json_file:
      data = json.load(json_file)
      if not data['access_token']:
        return self._login()
      else:
        return data['access_token']


# Credentials 
email = "admin@example.com"
password = "Admin@123"
login_url = "http://example.local/login"

# Make an Authentication
auth = Auth(email=email, password=password, login_url=login_url)

def getData(url):
  try:
    # 1. Load saved acces token 
    access_token = auth.getAccessToken()

    # 2. Append to request header 
    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer {access_token}'.format(access_token=access_token)})

    # 3. Make request with access_token
    response = session.get(url)
    response.raise_for_status()

    data = response.json()

    # 4 Proccess data
    print("Get data success.")
    print(data)

  except requests.exceptions.HTTPError as errh:
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)


if __name__ == "__main__":
  url = 'http://example.local/products'
  getData(url)
