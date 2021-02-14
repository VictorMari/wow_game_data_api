import logging
from logging import config as logConfig
import loggerConfig


logConfig.dictConfig(loggerConfig.logger_config)
log = logging.getLogger("debug")

import requests 

class Token:
    def __init__(self):
        pass

    def validate(self):
        pass

    def getHeaders(self):
        pass



class BattlenetOauth:
    def __init__(self, region, client_id, secret):
        self.client = client_id
        self.secret = secret
        self.region = region
        self.baseUrl = f"https://{region}.battle.net"

        #paths
        self.token_path = "/oauth/token"
        self.token_validation_path = "/oauth/check_token"

    def application_authentication(self):
        reqData = {
            "url": f"{self.baseUrl}{self.token_path}",
            "files":{
                "grant_type": (None, "client_credentials")
            },
            "auth": (self.client, self.secret)
        }

        tokenRequest = requests.post(**reqData)

        try:
            tokenRequest.raise_for_status()
            return tokenRequest.json()

        except Exception as e:
            print(e)


    def user_authentication(self):
        raise Exception("Authorization code flow not implemented")


if __name__ == "__main__":
    client = BattlenetOauth("eu","f0eff582ba304d22881d664aaf0229f2", "7H7xZHOQ6SitwwiSisStcbtKCdxRogCY")
    token_data = client.application_authentication()

    print(token_data)