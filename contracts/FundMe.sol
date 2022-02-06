// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address payable public owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) {
        owner = payable(msg.sender);
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can access this function");
        _;
    }

    function fund() public payable {
        uint256 minimumUSD = 25 * 10**18;
        require(getUSDValue(msg.value) >= minimumUSD, "Minimum deposit of $25");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getETHUSDPrice() public view returns (uint256) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10**10);
    }

    function getUSDValue(uint256 ethQuantity) public view returns (uint256) {
        uint256 ethusdPrice = getETHUSDPrice();
        uint256 ethQuantityUSDValue = (ethusdPrice * ethQuantity) / 10**18;
        return ethQuantityUSDValue;
    }

    function withdraw() public payable onlyOwner {
        owner.transfer(address(this).balance);
        for (uint256 i = 0; i < funders.length; i++) {
            addressToAmountFunded[funders[i]] = 0;
        }
        funders = new address[](0);
    }

    function getETHEntranceFee() public view returns (uint256) {
        uint256 minimumUSD = 25 * 10**18;
        uint256 price = getETHUSDPrice();
        uint256 precision = 1 * 10**18;
        return (minimumUSD * precision) / price;
    }
}
