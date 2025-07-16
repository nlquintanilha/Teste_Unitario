from calc import soma

def test_soma():
    """Test the soma function."""
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(10, 5) == 15
    assert soma(-5, -5) == -10

    