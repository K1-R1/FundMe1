import pytest
from brownie import accounts, config, network, exceptions

from scripts.general_scripts import get_account, deploy_mocks
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    
    account = get_account()
    fund_me = deploy_fund_me()
    eth_entrance_fee = fund_me.getETHEntranceFee() + 100
    
    tx1 = fund_me.fund({'from': account, 'value': eth_entrance_fee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == eth_entrance_fee

    tx2 = fund_me.withdraw({'from': account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
    
def test_only_owner_can_withdraw():
    if not config['networks'][network.show_active()]['local'] is True:
        pytest.skip('Only tested on local networkss')

    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(ValueError):
        fund_me.withdraw({"from": bad_actor})