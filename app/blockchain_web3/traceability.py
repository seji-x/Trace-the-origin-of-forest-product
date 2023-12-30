import json
import logging
import os
import uuid

from app.blockchain_web3.actor_provider import ActorProvider
from app.blockchain_web3.product_provider import ProductProvider
from app.blockchain_web3.provider import Web3Provider
from django.conf import settings

logger = logging.getLogger(__name__)


class TraceabilityProvider(Web3Provider):

    def __init__(self, path_abi=None, chain_id=None, web3_provider=None, address_contract=None):
        path_abi = path_abi if path_abi else os.path.join(os.getcwd(), "app/abi/traceability.txt")
        with open(path_abi, 'r', encoding='utf-8') as f:
            abi = f.read()

        factory_abi = json.loads(abi)
        web3_provider = web3_provider if web3_provider else settings.WEB3_PROVIDER
        address_contract = address_contract if address_contract else settings.ADDRESS_CONTRACT_TRACEABILITY

        super().__init__(web3_provider, address_contract)
        self.chain_id = chain_id if chain_id else settings.CHAIN_ID
        self.contract = self.w3.eth.contract(address=address_contract, abi=factory_abi)

    def get_info_product(self, product_id):
        data = self.contract.functions.seekAnOrigin(product_id).call()
        result = []
        for item in data:
            result += [
                {"product": ProductProvider.convert_data(item[0]), "actor": ActorProvider.convert_data_user(item[0])}]
        return result

    def buy_product_in_market(self, product_id, id_trans, buyer, quantity):
        function = self.contract.functions.buyItemOnMarketplace(product_id, id_trans, buyer, quantity)
        return self.sign_and_send_transaction(function)

    def get_transaction_by_id(self, trans_id):
        return self.contract.functions.getTransactionById(trans_id).call()
