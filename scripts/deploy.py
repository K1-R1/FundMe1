from brownie import FundMe, MockV3Aggregator, network, config
from .general_scripts import get_account, deploy_mocks

def deploy_fund_me():
    account = get_account()
    
    _network = network.show_active()
    print(f"Active network: {_network}")
    if config['networks'][_network]['local'] is True:
        deploy_mocks()
        eth_usd_price_feed = MockV3Aggregator[-1].address
    else:
        eth_usd_price_feed = config['networks'][_network]['eth_usd_price_feed']

    fund_me = FundMe.deploy(eth_usd_price_feed, {'from': account}, 
                  publish_source=config['networks'][_network]['verify'])
    
    return fund_me

def main():
    deploy_fund_me()