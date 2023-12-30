import json
import os.path
import uuid

from eth_typing import Address

from app.blockchain_web3.provider import Web3Provider
from django.conf import settings


class ActorProvider(Web3Provider):

    def __init__(self, path_abi=None, chain_id=None, web3_provider=None, address_contract=None):
        path_abi = path_abi if path_abi else os.path.join(os.getcwd(), "app/abi/actor.txt")
        with open(path_abi, 'r', encoding='utf-8') as f:
            abi = f.read()

        factory_abi = json.loads(abi)
        web3_provider = web3_provider if web3_provider else settings.WEB3_PROVIDER
        address_contract = address_contract if address_contract else settings.ADDRESS_CONTRACT_ACTOR_MANAGER

        super().__init__(web3_provider, address_contract)
        self.chain_id = chain_id if chain_id else settings.CHAIN_ID
        self.contract = self.w3.eth.contract(address=address_contract, abi=factory_abi)

    def create_actor(self, user_id: str, address, role, name, real_address):
        function = self.contract.functions.create(user_id, Address(address), role, name, real_address)
        return self.sign_and_send_transaction(function)

    def update_actor(self, user_id: str, name, real_address):
        function = self.contract.functions.updateActor(user_id, name, real_address)
        return self.sign_and_send_transaction(function)

    def get_actor_by_id(self, user_id):
        return self.contract.functions.getActorById(user_id).call()

    def get_ids_by_role(self, role):
        return self.contract.functions.getIdsByRole(role).call()

    def deposited(self, user_id: str, amount: int):
        function = self.contract.functions.deposit(user_id, amount)
        return self.sign_and_send_transaction(function)

    def withdraw(self, user_id: str, amount: int):
        function = self.contract.functions.withdraw_balance(user_id, amount)
        return self.sign_and_send_transaction(function)

    @staticmethod
    def convert_data_user(data):
        return {
            'id': data[0],
            'owner': data[1],
            "role": data[2],
            'balance': data[3],
            'name': data[4],
            'real_address': data[5]
        }


if __name__ == "__main__":
    # actor_provider = ActorProvider().get_actor_by_id("e1bd3c7b-07b6-407b-afa3-041edf3bfe91")
    # print(actor_provider)
    # ActorProvider().deposited(user_id="68e144e4-9667-4187-98d3-2738c8a2927e", amount=100000)
    actor_provider = ActorProvider().get_actor_by_id("60b96988-dcb0-4afc-8f6d-a65f99a06995")
    # actor_provider = ActorProvider()
    print(actor_provider)
    # id = uuid.uuid4().__str__()
    # tx_hash = actor_provider.create_actor(user_id=id,
    #                                       address='0xe75DB3f37A05858507D469f896A4A982F7E1C302', role=0,
    #                                       hash_info="eyduYW1lJzogTm9uZSwgJ2F2YXRhcic6IE5vbmUsICdwaG9uZSc6IE5vbmUsICdhZGRyZXNzX3JlYWwnOiBOb25lfQ")
    # actor_provider = ActorProvider().get_actor_by_id(id)
    # print(actor_provider)
