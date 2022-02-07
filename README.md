# FundMe1

## A smart contract that allows anyone to fund it, but only the owner to withdraw.
The contract uses chainlink's AggregatorV3Interface to get current USD denominanated ETH prices, and ensure that any deposits are of sufficent USD value.

It then allows only the account that deployed the contract to access the deposited funds, before resetting an array and mapping of funders and their deposited quantities.

The contract can be deployed locally, to test networks, or to an ethereum mainnet for, as such accommadtion for each are made in the brownie deployment process.

Testing is also performed on the aforementioned networks, with some test only running locally.

### Made with
- solidity 0.8
- python 3.7
- brownie 

### Deployed to
- local ganache network
- rinkeby test network
- ethereum mainnet fork

