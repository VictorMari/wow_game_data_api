from api_resources.Realm import Realm
from api_resources.ConnectedRealm import ConnectedRealm
from api_resources.AuctionHouse import AuctionHouse
import logging

log = logging.getLogger("")


class GameDataApi:

    def __init__(self, region, token):
        self.baseUrl = f"https://{region}.api.blizzard.com"
        self.token = token

    def achivements(self):
        raise Exception(" api not implemented")

    def auction_house(self, realm_id):
        Auction_house_resource = AuctionHouse(realm_id, self.baseUrl, self.token)
        return Auction_house_resource

    def azerite(self):
        raise Exception(" api not implemented")

    def connected_realms(self):
        connected_realm_resource = ConnectedRealm(self.baseUrl, self.token)
        return connected_realm_resource

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
        realm_resource = Realm(self.baseUrl, self.token)
        return realm_resource

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


def realm_index_test():
    from oauth_flows.ClientCredentials import (
        FsTokenCache,
        OauthBattlenet
    )
    import os
    from dotenv import load_dotenv
    load_dotenv()

    tokenRepo = FsTokenCache("eu", "./data")
    oauth = OauthBattlenet(tokenRepo, os.getenv("CLIENT"), os.getenv("SECRET"))

    token = oauth.get_authorized_token()
    blizz_client = GameDataApi("eu", token.access_token)

    params = {
        "namespace": "dynamic-eu",
        "locale": "es_ES"
    }
    connectedRealms_index = blizz_client.connected_realms().index(params=params)
    for realm in connectedRealms_index:
        print(realm)


if __name__ == "__main__":
    realm_index_test()
