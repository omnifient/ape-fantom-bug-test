

def test_this_works(usdc):
    assert usdc != ""


def test_this_fails1(erc20_usdc1):
    assert erc20_usdc1.address != 0


def test_this_fails2(erc20_usdc2):
    assert erc20_usdc2.address != 0
