from brownie import FundMe
from .general_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    eth_entrance_fee = fund_me.getETHEntranceFee()
    print(f"The current entry fee is: {eth_entrance_fee / (10**18)}ETH or {eth_entrance_fee}")
    print('Funding')
    fund_me.fund({'from': account, 'value': eth_entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({'from': account})

def main():
    fund()
    withdraw()
