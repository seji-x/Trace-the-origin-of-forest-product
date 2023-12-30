import json
import os

from app.blockchain_web3.provider import Web3Provider
from django.conf import settings


class ProductProvider(Web3Provider):

    def __init__(self, path_abi=None, chain_id=None, web3_provider=None, address_contract=None):
        path_abi = path_abi if path_abi else os.path.join(os.getcwd(), "app/abi/product.txt")
        # breakpoint()
        with open(path_abi, 'r', encoding='utf-8') as f:
            abi = f.read()

        factory_abi = json.loads(abi)
        web3_provider = web3_provider if web3_provider else settings.WEB3_PROVIDER
        address_contract = address_contract if address_contract else settings.ADDRESS_CONTRACT_PRODUCT_MANAGER

        super().__init__(web3_provider, address_contract)
        self.chain_id = chain_id if chain_id else settings.CHAIN_ID
        self.contract = self.w3.eth.contract(address=address_contract, abi=factory_abi)

    def create_product(self, product_id, product_type, price, quantity, status, owner, image, name, trans_id=""):
        function = self.contract.functions.create(product_id, product_type, price, quantity, trans_id, status, owner,
                                                  image, name)
        tx_hash = self.sign_and_send_transaction(function)
        return tx_hash

    def update_product(self, product_id, price, quantity, name, image):
        function = self.contract.functions.update(product_id, price, quantity, name, image)
        tx_hash = self.sign_and_send_transaction(function)
        return tx_hash

    def get_product_by_id(self, product_id):
        return self.convert_data(self.contract.functions.readOneProduct(product_id).call())

    def get_product_of_user(self, user_id: str):
        products = self.contract.functions.getProductOfUser(user_id).call()
        converted_data = []
        for item in products:
            converted_data.append(self.convert_data(item))

        return converted_data

    def get_product_all(self):
        products = self.contract.functions.getAllProduct().call()
        converted_data = []
        for item in products:
            converted_data.append(self.convert_data(item))

        return converted_data

    @staticmethod
    def convert_data(data):
        return {
            "id": data[0],
            "product_type": data[1],
            "price": data[2],
            "quantity": data[3],
            "owner": data[4],
            "transaction": data[5],
            "status": data[6],
            'image': data[7],
            'name': data[8]
        }
