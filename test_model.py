import pytest

def test_model_addTag():
    aBed = Bed()
    assert aBed.getTags() == []
    newTag = 'Backyard'

    aBed.addTag(newTag)
    assert aBed.getTags() == ['Backyard']
