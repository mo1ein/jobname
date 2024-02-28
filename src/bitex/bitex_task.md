# Interview Assignment for Backend/Blockchain Engineer

## Objective:
Design and implement an API that allows users to store key-value pairs in a smart contract and retrieve values by providing the corresponding keys.

## Requirements:

1. Write a smart contract in Solidity that can store key-value pairs and retrieve values using keys. The smart contract should have functions for setting key-value pairs and getting values by keys. Both key and values are integers.
<br />
<br />
2. Set up a project to interact with the smart contract. Include necessary dependencies and configurations in the project.
<br />
<br />
3. Deploys the smart contract to a local Ethereum test network (e.g., Ganache, Hardhat, Anvil).
<br />
<br />
4. Use the ABI and contract address to create an instance of the smart contract.
<br />
<br />
5. Design and implement the API with the following endpoints:
 - POST `/store`: Stores a key-value pair in the smart contract.
Request Body: ``{ "key": "<key>", "value": "<value>" }``
Response: { "success": true, "message": "Key-value pair stored successfully." }

 - GET `/retrieve?key=<key>`: Retrieves the value corresponding to the provided key from the smart contract.
Response: `{ "key": "<key>", "value": "<value>" }`

6. Provide documentation on how to set up and run the project
<br />
<br />

7. (Optional) Write unit tests for the API endpoints and smart contract functions.
