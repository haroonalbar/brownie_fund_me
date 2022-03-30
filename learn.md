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

