from web3 import Web3


url = 'https://mainnet.infura.io/v3/a10be469e0ba4d7aa0d391e19628e8b7'
web3 = Web3(Web3.HTTPProvider(url))
lates_block = web3.eth.get_block('latest')
print("Latest of block of etherium block chain: ", lates_block)
block_transaction_count = web3.eth.get_block_transaction_count(18691733)
print("Number of transactions happened in this block: " , block_transaction_count)
transaction_fee = web3.eth.fee_history(4,'latest',None)
print("Transaction fee history in the block: ", transaction_fee )
