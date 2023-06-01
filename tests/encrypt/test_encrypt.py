import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(3, 3)

    with pytest.raises(TypeError):
        encrypt_message("banana", "abc")

    assert encrypt_message("banana", 3) == "nab_ana"
    assert encrypt_message("banana", 4) == "an_anab"
    assert encrypt_message("banana", 15) == "ananab"
