from texto import contar_caracteres

def test_contar_caracteres():
    """Test the contar_caracteres function."""
    assert contar_caracteres("Hello") == 5
    assert contar_caracteres("") == 0
    assert contar_caracteres("Python") == 6
    assert contar_caracteres("12345") == 5
    assert contar_caracteres("!@#$%^&*()") == 10

