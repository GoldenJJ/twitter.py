import requests
import json

class Client():
    def __init__(self, token: str = None) -> None:
        self.token = token
        self.header = {"Authorization" : f"Bearer {self.token}"}
        """Client class"""
    
    def help(self):
        statuscodes = [
            "Twitter API HTTP status codes", 
            "200: OK","304: Not Modified", 
            "400: Bad Request", 
            "401: Unauthorized", 
            "403: Forbidden", 
            "404: Not Found", 
            "406: Not Acceptable", 
            "410: Gone", 
            "422: Unprocessable Entity", 
            "429: Too Many Requests", 
            "500: Internal Server Error", 
            "502: Bad Gateway", 
            "503: Service Unavailable", 
            "504: Gateway Timeout"
            ]
        print("\n".join(statuscodes))
        """Help command"""

    def get_user(self, username: str) -> None:
        if username.startswith("@"):
            raise Exception("Must be the username only")
        try:
            resp = requests.get(f"https://api.twitter.com/2/users/by/username/{username}", 
            headers=self.header)
            data = json.loads(resp.text)
            print(resp.status_code, data)
        except Exception as errorcode:
            raise errorcode
        """Getuser command, makes a request to the twitter api for a user"""

    def get_users(self, *usernames: str) -> None:
        if "@" in usernames:
            raise Exception("Must be the username only")
        try:
            newids = ",".join(usernames)
            resp = requests.get(f"https://api.twitter.com/2/users/by/username/{newids}", 
            headers=self.header)
            data = json.loads(resp.text)
            print(resp.status_code, data)
        except Exception as errorcode:
            raise errorcode
        """Getusers command, makes a request to the twitter api for a group of users"""


    def get_tweet(self, id: int) -> None:
        if type(id) == str:
            raise Exception("id must be an int not a string")
        try:
            resp = requests.get(f"https://api.twitter.com/2/tweets?ids={id}",
            headers=self.header)
            data = json.loads(resp.text)
            print(resp.status_code, data)
        except Exception as errorcode:
            raise errorcode
        """Getuser command, makes a request to the twitter api for a tweet"""

    def get_tweets(self, *ids: int) -> None:
        try:
            newids = ",".join(ids)
            resp = requests.get(f"https://api.twitter.com/2/tweets?ids={newids}", 
            headers=self.header)
            data = json.loads(resp.text)
            print(resp.status_code, data)
        except Exception as errorcode:
            raise errorcode
        """Getusers command, makes a request to the twitter api for a group of tweets"""
