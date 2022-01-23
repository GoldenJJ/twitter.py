import requests
import json

class Client:
    def __init__(
        self,
        token: str
        ) -> None:
        self.token = token
        self.header = {
            "Authorization" : f"Bearer {self.token}"
            }
        """
        A client class that has methods to access the twitter API.
        
        Parameters
        ----------
        token: :class: `str`
            Bare token used for authorization
        """
    
    def _help(self):
        status_codes = [
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
        print("\n".join(status_codes))

    def get_users(
        self,
        *usernames: str
        ) -> str:
        """
        Gets a user by username.

        Parameters
        ----------
        username: :class: `str`
        """
        # turn usernames into A list of usernames

        usernames = ",".join(usernames)
        usernames = usernames.split()
        

        for user in usernames:
            if user.startswith("@"):
                user = user[1:]
            try:
                resp = requests.get(
                    f"https://api.twitter.com/2/users/by/username/{user}", 
                headers=self.header
                )
                data = json.loads(resp.text)
                print(data)

            except Exception as errorcode:
                raise errorcode

    def get_tweet(
        self,
        id: int
        ) -> str:
        """
        Gets a tweet by ID.

        Parameters
        ----------
        id: :class: `int`
        """
        if not isinstance(id, int):
            raise Exception(f"id must be an int, not a {type(id).__name__}")

        try:
            resp = requests.get(
                f"https://api.twitter.com/2/tweets?ids={id}",
                headers=self.header
                )
            data = json.loads(resp.text)

            return data

        except Exception as errorcode:
            raise errorcode

    def get_tweets(
        self,
        *ids: int
        ) -> str:
        """
        Gets tweets by IDs
        
        Parameters
        ----------
        ids: :class: `int`
        """
        try:
            new_ids = ",".join(ids)
            resp = requests.get(
                f"https://api.twitter.com/2/tweets?ids={new_ids}", 
                headers=self.header
                )
            data = json.loads(resp.text)

            return data

        except Exception as errorcode:
            raise errorcode