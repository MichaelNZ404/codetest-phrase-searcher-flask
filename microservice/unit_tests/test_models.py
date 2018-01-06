import pytest

from microservice.models import Glossary

@pytest.fixture(scope="session")
def get_glossary():
    ''' load glossary once for all tests '''
    return Glossary()

@pytest.mark.parametrize('searchword, expected', [
    ('mood disorder depressive', ["depressive disorder", "mood disorder"]),
    ('I have a sore throat and headache.', ['headache', 'sore throat']),
    ('I throat throat a throat and headache.', ['headache']),
])
def test_search(searchword, expected):
    '''search within the glossary for terms'''
    glossary = get_glossary()
    assert glossary.search(searchword) == expected
