from Battlenet import Battlenet
from Battlenet import Token
from pathlib import Path
from logging import config as logConfig
import loggerConfig
import logging
import json

logConfig.dictConfig(loggerConfig.logger_config)
log = logging.getLogger("debug")


class Resource:

    def __init__(self):
        pass

    def get(self):
        raise Exception("Resource get not implemented")
    
    def index(self):
        raise Exception("Resource index not implemented")

class TokenProvider:
    def __init__(self):
        pass

    def retrieveToken(self):
        raise Exception("Retrieve token method not implemented")

    def saveToken(self):
        raise Exception("Save token method not implemented")


class DbTokenProvider(TokenProvider):
    def __init__(self):
        pass

class FsTokenProvider(TokenProvider):
    def __init__(self, region, basePath):
        self.region = region
        self.basePath = Path(basePath).joinpath(region)
        
        if not self.basePath.exists():
            self.basePath.mkdir(exist_ok=True, parents=True)
            log.info(f"Created folder {self.basePath}")

    def retrieveToken(self): # user param to get specific token from user
        token_path = self.basePath.joinpath("token.json")
        if token_path.exists():
            with token_path.open() as token_file:
                token_json = token_file.read()
                if not token_json == "":
                    token_data = json.loads(token_json)
                    log.info(f"Retrieved token {token_path}")
                    return Token(**token_data)
    
    def saveToken(self, token):
        token_path = self.basePath.joinpath("token.json")
        token_dict = {
            "access_token": token.access_token,
            "token_type": token.token_type,
            "expires_in": token.expires_in
        }
        token_path.touch()
        with token_path.open("w+") as token_file:
            token_file.write(json.dumps(token_dict))
            log.info(f"Saved token to {token_path}")


class OauthBattlenet:
    def __init__(self, tokenProvider, client_id, secret):
        # retrieves token from custom storage of battlenet
        self.region = tokenProvider.region
        self.client = client_id
        self.secret = secret
        self.BattlenetClient = Battlenet(self.region, client_id, secret)
        self.tokenProvider = tokenProvider

    def getAuthorizedToken(self):
        current_token = self.tokenProvider.retrieveToken()
        token_meta = self.BattlenetClient.validate_token(current_token)
        if token_meta:
            return current_token

        new_token = self.BattlenetClient.application_authentication()
        self.tokenProvider.saveToken(new_token)

        


        
        # pull token from provider
        # verify token
        # if not valid create new one
        # save 
        # return


class GameDataApi:

    def __init__(self, region, Token):
        # token inspance provided in constructor

        # create OauthAuthenticator instance

        # do a server oauth flow 

        # set the returned token as an instance field
        pass


    def achivements(self):
        raise Exception(" api not implemented")

    def auction_house(self, realm_id):
        raise Exception(" api not implemented")

    def azerite(self):
        raise Exception(" api not implemented")

    def connected_realm(self):
        raise Exception(" api not implemented")

    def covenants(self):
        raise Exception(" api not implemented")

    def creatures(self):
        raise Exception(" api not implemented")

    def guild_crest(self):
        raise Exception(" api not implemented")

    def items(self):
        raise Exception(" api not implemented")

    def jourlan(self):
        raise Exception(" api not implemented")

    def media_search(self):
        raise Exception(" api not implemented")

    def modified_crafting(self):
        raise Exception(" api not implemented")

    def mounts(self):
        raise Exception(" api not implemented")

    def mythic_keystone_afixes(self):
        raise Exception(" api not implemented")
    
    def mythic_keystone_dungeons(self):
        raise Exception(" api not implemented")

    def mythic_keystone_leaderboards(self):
        raise Exception(" api not implemented")

    def mythic_raid_leaderboards(self):
        raise Exception(" api not implemented")

    def pets(self):
        raise Exception(" api not implemented")

    def playable_class(self):
        raise Exception(" api not implemented")

    def playable_race(self):
        raise Exception(" api not implemented")

    def playable_specialization(self):
        raise Exception(" api not implemented")

    def power_type(self):
        raise Exception(" api not implemented")

    def professions(self):
        raise Exception(" api not implemented")

    def pvp_seasson(self):
        raise Exception(" api not implemented")

    def pvp_tier_api(self):
        raise Exception(" api not implemented")

    def quest_api(self):
        raise Exception(" api not implemented")

    def realms(self):
        raise Exception(" api not implemented")

    def reputations(self):
        raise Exception(" api not implemented")

    def spells(self):
        raise Exception(" api not implemented")

    def talents(self):
        raise Exception(" api not implemented")

    def tech_talent(self):
        raise Exception(" api not implemented")

    def wow_token(self):
        raise Exception(" api not implemented")




if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    tokenRepo = FsTokenProvider("eu", "./data")
    oauth = OauthBattlenet(tokenRepo, os.getenv("CLIENT"), os.getenv("Secret"))

    token = oauth.getAuthorizedToken()
    print(token)