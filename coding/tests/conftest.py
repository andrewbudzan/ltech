# author: andrii budzan
import pytest
from coding import constants


@pytest.fixture
def input_values_companies():
    return constants.companies


@pytest.fixture
def input_values_parcels():
    return constants.land_parcels
