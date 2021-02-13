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


class Token(Resource):
    def __init__(self):
        pass

    def validate(self):
        pass

    def generateNewToken(self):
        pass

    def getHeaders(self):
        pass


class DbTokenProvider:
    def __init__(self):
        pass

class FsTokenProvider:
    def __init__(self):
        pass

class OauthAuthenticator:
    def __init__(self):
        pass

    def server_oauth_flow(self):
        pass

class GameDataApi:

    def __init__(self):
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






