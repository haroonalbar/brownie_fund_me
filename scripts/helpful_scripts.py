from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVITONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCAHIN_ENVIRONMENT = ["development", "dog"]

# 8 because it follows ethusd pricefeed
DECIMALS = 8
STARTING_PRICE = 200000000000
# 2000*10**10


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCAHIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVITONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks ...")
    # we dont have to deploy every time
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed!")
