import requests
import json

class Client:
    def __init__(
        self,
        token: str = None
        ) -> None:
        self.token = token
        self.header = {
            "Authorization" : f"Bearer {self.token}"
            }
        """A client class that has methods to access the twitter api
        
        Parameters
        ----------
        token: :class: `str`
            Bare token used for authorization
        """
    
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
        """Help command
        gives http status codes"""

    def get_user(
        self,
    username: str
    ) -> None:
        """Gets a user by username
        Parameters
        ----------
        username: :class: `str`
        """
        if username.startswith("@"):
            raise Exception("Must be the username only")
        try:
            resp = requests.get(
                f"https://api.twitter.com/2/users/by/username/{username}", 
            headers=self.header
            )
            data = json.loads(resp.text)
            print(
                resp.status_code,
                data
                )
        except Exception as errorcode:
            raise errorcode

    def get_users(
        self,
        *usernames: str
        ) -> None:
        """Gets users by usernames
        Parameters
        ----------
        usernames: :class: `str`
        """
        if "@" in usernames:
            raise Exception("Must be the username only")
        try:
            newids = ",".join(usernames)
            resp = requests.get(
                f"https://api.twitter.com/2/users/by/username/{newids}", 
            headers=self.header
            )
            data = json.loads(resp.text)
            print(
                resp.status_code,
                data
                )
        except Exception as errorcode:
            raise errorcode


    def get_tweet(
        self,
        id: int
        ) -> None:
        """Gets a tweet by id
        Parameters
        ----------
        id: :class: `int`
        """
        if isinstance(
            id,
            str
            ):
            raise Exception("id must be an int not a string")
        try:
            resp = requests.get(
                f"https://api.twitter.com/2/tweets?ids={id}",
                headers=self.header
                )
            data = json.loads(resp.text)
            print(
                resp.status_code,
                data
                )
        except Exception as errorcode:
            raise errorcode

    def get_tweets(
        self,
    *ids: int
    ) -> None:
        """Gets tweets by ids
        Parameters
        ----------
        ids: :class: `int`
        """
        try:
            newids = ",".join(ids)
            resp = requests.get(
                f"https://api.twitter.com/2/tweets?ids={newids}", 
                headers=self.header
                )
            data = json.loads(resp.text)
            print(
                resp.status_code,
                data
                )
        except Exception as errorcode:
            raise errorcode
