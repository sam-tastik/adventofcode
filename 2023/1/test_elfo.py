import elfo


def test_trasforma_riga_singola_cifra():
    for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        assert num == elfo.trasforma_riga(num)


def test_trasforma_riga_singolo_numero_in_lettere():
    assert '1' == elfo.trasforma_riga("one")
    assert '2' == elfo.trasforma_riga("two")
    assert '3' == elfo.trasforma_riga("three")
    assert '4' == elfo.trasforma_riga("four")
    assert '5' == elfo.trasforma_riga("five")
    assert '6' == elfo.trasforma_riga("six")
    assert '7' == elfo.trasforma_riga("seven")
    assert '8' == elfo.trasforma_riga("eight")
    assert '9' == elfo.trasforma_riga("nine")
    


def test_trasforma_riga_two():
    assert '2' == elfo.trasforma_riga("two")


def test_trasforma_riga_two_one():
    assert '21' == elfo.trasforma_riga("twoone")


def test_trasforma_riga_2_one():
    assert '21' == elfo.trasforma_riga("2one")


def test_trasforma_riga_twone():
    assert '21' == elfo.trasforma_riga("twone")


