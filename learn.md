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
