from src.api_resources.Resource import Resource
from src.api_resources.Resource import execute_request


class AuctionHouse(Resource):
    def __init__(self, realm_id, baseUrl, token):
        self.baseUrl = baseUrl
        self.token = token
        self.ah_path = f"/data/wow/connected-realm/{realm_id}/auctions"

    def get(self, params):
        reqParams = {
            "url": f"{self.baseUrl}{self.ah_path}",
            "params": params,
            "headers":{
                "Authorization": f"Bearer {self.token}"
            },
            "method": "GET"
        }

        response = execute_request(reqParams)
        return response
        
