import imp
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCAHIN_ENVIRONMENT,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # pass pricefeed address to fundme
    # if  in persistant network like rinkeby use this address otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCAHIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    # for test to get fundme
    return fund_me


def main():
    deploy_fund_me()
