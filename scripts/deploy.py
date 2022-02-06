from brownie import FundMe, MockV3Aggregator, network, config
from .general_scripts import get_account, deploy_mocks

def deploy_fund_me():
    account = get_account()
    _network = network.show_active()
    print(f"Active network: {_network}")
    if _network != 'development':
        eth_usd_price_feed = config['networks'][_network]['eth_usd_price_feed']
    else:
        deploy_mocks()
        eth_usd_price_feed = MockV3Aggregator[-1].address
    FundMe.deploy(eth_usd_price_feed, {'from': account}, 
                  publish_source=config['networks'][_network]['verify'])


def main():
    deploy_fund_me()