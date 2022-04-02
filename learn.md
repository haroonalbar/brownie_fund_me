Brownie fund me
        cd ..
        mkdir brownie_fund_me
        cd brownie_fund_me
        code .

        brownie init

create FundMe.sol in contracts
        brownie console *it will show error importing contracts sirectly from chainlink so we change it to its github reposatory*

create brownie-config.yaml file
        we can add dependencies
        and set @chainlink to the github dependency
        brownie compile *works properly

create deploy.py in scipts
create helpful_scripts.py for adding getaccount()
in yaml file make dotenv and wallets
create .env and copy the .env of brownie simple storage

for impoting from other scripts and packages.
depending on the python version we may need to create a new file in scripts __init__.py
may be you dont need it but just in case we might as well create it

brownie run deploy.py *for deploying it*
the deployed contract cannot me seen in ether scan for the public to intract with
so verify and publish the smart contract to eather scan
etherscan doesnt know about @cahinlink importing
to solve this go to etherscan.io and login and make a api key token
set the api key an env
and publish_source=True in deploy line

deploy it again and go to rinkeby etherscan
we can see the contract there and intract with it in etherscan by connecting metamask

to work with the local cahin is difficult because of pricefeed in the fundme smartcontract 
that is made for the rinkeby network

2 ways to get around this problem
MOCK
FORK

we are going to use the mock method here

change the fundme smartcontract parameterise it
so the aggregatorV3 is not hard coded in fundme
brownie compile //to check if it is working perfectly
in yaml file add networks rinkeby price_feed_address=addressofrinkebypricefeed
we can also add kovan and mainnet if want Here

create new folder test in contracts to do mocks
goto https://github.com/smartcontractkit/chainlink-mix
create new mock contract in test aggregatorV3mock.sol
copy the code from the site
brownie compile

add verify in networks on yaml in rinkeby set True and in development set False
and set publish_source with config in deploy.py

open ganache ui and create a new local chain
brownie run deploy.py
        it will automatically detect your local chain and deploy in it

for the brownie to save changes in the local chain add a new network

        brownie networks add Ethereum networkname host=url chainid=chainid
        brownie networks add Ethereum ganache-local host=http://0.0.0.0:8545 chainid=5777

to delete
       
        brownie networks delete networkname



