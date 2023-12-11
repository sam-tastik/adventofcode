import elfo


def test_trasforma_riga_singola_cifra():
    assert elfo.trasforma_riga('1') == '1'
    for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        assert elfo.trasforma_riga(num) == num


def test_trasforma_riga_singola_piu_cifre():
    assert elfo.trasforma_riga('424242') == '424242'

def test_trasforma_numeri():
    assert elfo.trasforma_riga("one") == '1'
    assert elfo.trasforma_riga("two") == '2'
    assert elfo.trasforma_riga("three") == '3'
    assert '4' == elfo.trasforma_riga("four")
    assert '5' == elfo.trasforma_riga("five")
    assert '6' == elfo.trasforma_riga("six")
    assert '7' == elfo.trasforma_riga("seven")
    assert '8' == elfo.trasforma_riga("eight")
    assert '9' == elfo.trasforma_riga("nine")

def test_trasforma_two_one():
    assert elfo.trasforma_riga("twoone") == '21'


def test_trasforma_riga_2_one():
    assert '21' == elfo.trasforma_riga("2one")

def test_trasforma_riga_8_one():
    assert '81' == elfo.trasforma_riga("8one")


def test_trasforma_riga_threeone():
    assert '31' == elfo.trasforma_riga("threeone")

def test_trasforma_riga_twone():
    assert '21' == elfo.trasforma_riga("twone")


def test_trasforma_riga_oneight():
    assert '18' == elfo.trasforma_riga("oneight")

def test_trasforma_one_two():
    assert elfo.trasforma_riga("onetwo") == '12'

