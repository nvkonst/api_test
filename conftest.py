import pytest
from fixture.api import API


@pytest.fixture
def api():
    fixture = API(base_url="https://www.lenvendo.ru/api")
    return fixture
