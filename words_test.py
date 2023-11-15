import pytest

import words


def test_1(monkeypatch, capsys, detector):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sorted_list = words.main()
    if detector == 1:
        assert sorted_list == ['0', 'üüüüü']
    elif detector <= 3:
        assert sorted_list == ['üüüüü']
    else:
        assert sorted_list == []


def test_2(monkeypatch, capsys, detector):
    if detector == 1:
        print(f'test_2 nicht relevant für Schritt {detector}')
        assert False
    else:
        inputs = iter(['2', 'Badabum', 'Päng'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sorted_list = words.main()
        if detector == 2:
            assert sorted_list == ['Päng', 'Badabum', 'üüüüü']
        elif detector == 3:
            assert sorted_list == ['Badabum', 'Päng', 'üüüüü']
        else:
            assert sorted_list == ['Badabum', 'Päng']


def test_3a(monkeypatch, capsys, detector):
    if detector <= 2:
        print(f'test_3a nicht relevant für Schritt {detector}')
        assert False
    else:
        inputs = iter(['2', 'Krach', 'Badabum'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sorted_list = words.main()

        if detector == 3:
            assert sorted_list == ['Badabum', 'Krach', 'üüüüü']
        else:
            assert sorted_list == ['Badabum', 'Krach']


def test_3b(monkeypatch, capsys, detector):
    if detector <= 2:
        print(f'test_3b nicht relevant für Schritt {detector}')
        assert False
    else:
        inputs = iter(['4', 'Krach', 'Päng', 'Boom', 'Päng'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sorted_list = words.main()

        if detector == 3:
            assert sorted_list == ['Boom', 'Krach', 'Päng', 'Päng', 'üüüüü']
        else:
            assert sorted_list == ['Boom', 'Krach', 'Päng']


def test_4a(monkeypatch, capsys, detector):
    if detector <= 3:
        print(f'test_4a nicht relevant für Schritt {detector}')
        assert False
    else:
        inputs = iter(['3', 'Päng', 'Badabum', 'Badabum'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sorted_list = words.main()
        assert sorted_list == ['Badabum', 'Päng']


def test_4b(monkeypatch, capsys, detector):
    if detector <= 3:
        print(f'test_4b nicht relevant für Schritt {detector}')
        assert False
    else:
        inputs = iter(['5', 'Krach', 'Päng', 'Krach', 'Krach', 'Badabum'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sorted_list = words.main()
        assert sorted_list == ['Badabum', 'Krach', 'Päng']


@pytest.fixture
def detector(monkeypatch, capsys):
    step = 0
    inputs = iter(['5', 'Eins', 'Zwei', 'Drei', 'Zwei', 'Vier'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sorted_list = words.main()
    if sorted_list[0] == '5':
        step = 1
    elif sorted_list[0] == 'Vier':
        step = 2
    elif len(sorted_list) > 5 and sorted_list[5] == 'üüüüü':
        step = 3
    else:
        step = 4
    print(f'Schritt {step} wird getestet')
    return step