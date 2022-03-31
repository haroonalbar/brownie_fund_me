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
