// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WoodManagement {
    address public owner;
    
    struct Wood {
        string name;
        uint quantity;
    }
    
    mapping(string => Wood) public woods;

    event WoodAdded(string name, uint quantity);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function addWood(string memory _name, uint _quantity) public onlyOwner {
        require(_quantity > 0, "Quantity must be greater than 0");
        require(bytes(_name).length > 0, "Wood name cannot be empty");

        if (woods[_name].quantity == 0) {
            woods[_name] = Wood(_name, _quantity);
        } else {
            woods[_name].quantity += _quantity;
        }

        emit WoodAdded(_name, _quantity);
    }

    function getWoodQuantity(string memory _name) public view returns (uint) {
        return woods[_name].quantity;
    }
}
