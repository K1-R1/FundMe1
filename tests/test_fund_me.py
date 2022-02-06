from scripts.general_scripts import get_account, deploy_mocks
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    
    account = get_account()
    fund_me = deploy_fund_me()
    eth_entrance_fee = fund_me.getETHEntranceFee()
    
    tx1 = fund_me.fund({'from': account, 'value': eth_entrance_fee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == eth_entrance_fee

    tx2 = fund_me.withdraw({'from': account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
    
    