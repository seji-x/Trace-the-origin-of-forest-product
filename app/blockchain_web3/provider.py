import re
from time import sleep

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

from django.conf import settings


class Web3Provider(object):

    def __init__(self, provider=None, contract_address=None):
        if re.match(r'^https*:', provider):
            self.w3 = Web3(Web3.HTTPProvider(provider, request_kwargs={"timeout": 60}))
        elif re.match(r'^ws*:', provider):
            self.w3 = Web3(Web3.WebsocketProvider(provider))
        elif re.match(r'^/', provider):
            self.w3 = Web3(Web3.IPCProvider(provider))
        else:
            raise RuntimeError("Unknown provider type " + provider)
        self.contract_address = contract_address
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        if not self.w3.is_connected():
            raise RuntimeError("Unable to connect to provider at " + provider)

    def check_connection(self):
        return self.w3.is_connected()

    def get_transaction_count(self, address):
        return self.w3.eth.get_transaction_count(address)

    def sign_and_send_transaction(self, func):
        account = Account.from_key('7b4bd6f0fd9472379cb51a0b9d7a7c7439446ef1f4fc8bb90395f964a57da751')
        nonce = self.get_transaction_count(account.address)
        gas = 5000000
        gas_price = self.w3.eth.gas_price

        tx_data = func.build_transaction({'chainId': 23011913, 'gas': gas, 'gasPrice': gas_price})

        transaction = {
            'to': self.contract_address,
            'value': 0,
            'gas': gas,
            'gasPrice': gas_price,
            'nonce': nonce,
            'data': tx_data['data'],
            'chainId': 23011913
        }

        signed_transaction = self.w3.eth.account.sign_transaction(transaction,
                                                                  '7b4bd6f0fd9472379cb51a0b9d7a7c7439446ef1f4fc8bb90395f964a57da751')
        tx_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        receipt = self.wait_for_transaction_receipt(tx_hash)
        print(receipt)
        if receipt['status'] == 0:
            raise ValueError("chua ghi duoc block")

        print("Transaction confirmed in block", receipt['blockNumber'])
        return tx_hash.hex()

    def wait_for_transaction_receipt(self, tx_hash):
        while True:
            try:
                receipt = self.w3.eth.get_transaction_receipt(tx_hash)
                if receipt is not None:
                    return receipt
            except Exception as e:
                print("Error checking transaction receipt:", e)
            sleep(0.1)
