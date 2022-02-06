from brownie import MockV3Aggregator, network, accounts, config

decimals = 8
starting_value = 2500

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['dev_account_1']['private_key'])

def deploy_mocks():
    if not len(MockV3Aggregator):
        MockV3Aggregator.deploy(decimals, starting_value * 10 ** 8, {'from': get_account()})
    print('Mocks deployed\n')
    