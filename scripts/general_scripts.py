from brownie import network, accounts, config

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['dev_account_1']['private_key'])