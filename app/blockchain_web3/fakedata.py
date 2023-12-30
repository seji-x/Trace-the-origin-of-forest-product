import uuid

from app.blockchain_web3.actor_provider import ActorProvider
from app.blockchain_web3.product_provider import ProductProvider
from app.blockchain_web3.traceability import TraceabilityProvider
from eth_account import Account

actor = ActorProvider(path_abi='../abi/actor.txt', address_contract='0x6F950FF9d3f3A4F992321c0A07F16dc623CbcAdf',
                      chain_id=23011913, web3_provider="https://stylus-testnet.arbitrum.io/rpc")

product = ProductProvider(path_abi='../abi/product.txt', address_contract='0x8d2ABe91980E8096e1EA465f69efADB146d1C523',
                          chain_id=23011913, web3_provider="https://stylus-testnet.arbitrum.io/rpc")
traceability = TraceabilityProvider(path_abi='../abi/traceability.txt',
                                    address_contract='0xFd64A5BC2F61490264C6d42573491dB649D6da9B',
                                    chain_id=23011913, web3_provider="https://stylus-testnet.arbitrum.io/rpc")


def create_user(role, name, real_address):
    account = Account.create()
    address = account.address
    user_id = uuid.uuid4().__str__()
    actor.create_actor(user_id=user_id, address=address, role=role, name=name, real_address=real_address)
    return user_id


def deposited_actor(user_id):
    actor.deposited(user_id=user_id, amount=100000000)


def create_product(product_type, trans_id, owner, name, image):
    product_id = uuid.uuid4().__str__()
    product.create_product(product_id=product_id, quantity=1000, price=10, status=1,
                           product_type=product_type, trans_id=trans_id, owner=owner, name=name, image=image)
    return product_id


def buy_product(product_id, quantity, buyer):
    id_transaction = uuid.uuid4().__str__()
    traceability.buy_product_in_market(product_id=product_id, quantity=quantity, id_trans=id_transaction,
                                       buyer=buyer)
    return id_transaction


if __name__ == "__main__":
    account = Account.create()
    address = account.key.hex()
    usr = [create_user(0, "cty a", "aaa"), create_user(1, "cty b", "bbb"), create_user(2, "cty c", "ccc")]
    deposited_actor(usr[1])
    deposited_actor(usr[2])
    p1 = create_product(1, "", usr[0], "cay go c", "")
    t1 = buy_product(p1, 100, usr[1])
    p2 = create_product(2, t1, usr[1], "tu bep", "")
    t2 = buy_product(p2, 100, usr[2])
    p3 = create_product(3, t2, usr[2], "tu bep", "")
    print(p3)

    data = traceability.get_info_product(p3)
    for item in data:
        print(item)
        print(ProductProvider.convert_data(item[0]), ActorProvider.convert_data_user(item[1]))



