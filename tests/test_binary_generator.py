from binary_generator.binary_generator import binary_generator
import random


def test_binary_generator(monkeypatch):
    def fake_random(a, b):
        return a
    monkeypatch.setattr(random, "randint", fake_random)
    assert binary_generator(5) == '00000'
    # assert len(binary_generator(5)) == 5
    # assert binary_generator(5) == ''
