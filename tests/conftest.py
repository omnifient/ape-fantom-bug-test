from ape import Contract, accounts, project
from pytest import fixture

from .abis import ERC20


@fixture
def usdc():
    # https://ftmscan.com/token/0x04068da6c83afcfa0e13ba15a6696662335d5b75
    return "0x04068da6c83afcfa0e13ba15a6696662335d5b75"


@fixture
def erc20_usdc1(usdc):
    return Contract(usdc)


@fixture
def erc20_usdc2(usdc):
    return Contract(usdc, contract_type=ERC20)
