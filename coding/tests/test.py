# author: andrii budzan
import pytest

from coding.land_parcels import check_parent_id, check_parcels, find_all_related_companies,\
    find_all_related_parcels, get_land_parcels_for_company


@pytest.mark.functional
@pytest.mark.positive
@pytest.mark.parametrize('parent_id, comp_idx, expected', [
    ('c1', 2, 'c3'),
    ('c3', 4, 'c5'),
    ('c3', 5, 'c6'),
    ('c2', 3, 'c4'),
    ('c4', 3, None),
    ('c6', 0, None),
    ('c5', 1, None)
])
def test_check_parent_id(parent_id, comp_idx, expected, input_values_companies):
    assert isinstance(input_values_companies, list), f"expect {type(list)}, received: {type(input_values_companies)}"
    company = input_values_companies[comp_idx]
    assert isinstance(parent_id, str), f"expect {type(str)}, received: {type(parent_id)}"
    related_companies = check_parent_id(parent_id, company)
    assert related_companies == expected, f'{related_companies} != {expected}'


@pytest.mark.functional
@pytest.mark.positive
@pytest.mark.parametrize('company_id, parcel_idx, expected', [
    ('c1', 0, 'l1'),
    ('c2', 1, 'l2'),
    ('c3', 2, 'l3'),
    ('c4', 3, None),
    ('c5', 4, 'l5'),
    ('c5', 3, 'l4'),
    ('c6', 0, None),
])
def test_check_parcels(company_id, parcel_idx, expected, input_values_parcels):
    assert isinstance(input_values_parcels, list), f"expect {type(list)}, received: {type(input_values_parcels)}"
    parcel = input_values_parcels[parcel_idx]
    assert isinstance(company_id, str), f"expect {type(str)}, received: {type(company_id)}"
    related_parcel = check_parcels(company_id, parcel)
    assert related_parcel == expected, f'{related_parcel} != {expected}'


@pytest.mark.functional
@pytest.mark.positive
@pytest.mark.parametrize('company_id, expected', [
    ('c1', ['c1', 'c3', 'c5', 'c6']),
    ('c2', ['c2', 'c4']),
    ('c3', ['c3', 'c5', 'c6']),
    ('c4', ['c4']),
    ('c5', ['c5']),
    ('c6', ['c6'])
])
def test_find_all_related_companies(company_id, expected, input_values_companies):
    storage = list()
    assert isinstance(input_values_companies, list), f"expect {type(list)}, received: {type(input_values_companies)}"
    assert isinstance(company_id, str), f"expect {type(str)}, received: {type(company_id)}"
    assert isinstance(storage, list), f"expect {type(list)}, received: {type(storage)}"
    assert len(storage) == 0, f'storage is not empty'
    find_all_related_companies(company_id=company_id, companies=input_values_companies, storage=storage)
    assert storage == expected, f'{storage} != {expected}'


@pytest.mark.functional
@pytest.mark.positive
@pytest.mark.parametrize('companies_ids, expected', [
    (['c1', 'c3', 'c5', 'c6'], ['l1', 'l3', 'l4', 'l5']),
    (['c2', 'c4'], ['l2']),
    (['c3', 'c5', 'c6'], ['l3', 'l4', 'l5']),
    (['c4'], []),
    (['c5'], ['l4', 'l5']),
    (['c6'], [])
])
def test_find_all_related_companies(companies_ids, expected, input_values_parcels):
    storage_parcels = list()
    assert isinstance(input_values_parcels, list), f"expect {type(list)}, received: {type(input_values_parcels)}"
    assert isinstance(companies_ids, list), f"expect {type(list)}, received: {type(companies_ids)}"
    assert isinstance(storage_parcels, list), f"expect {type(list)}, received: {type(storage_parcels)}"
    assert len(storage_parcels) == 0, f'storage is not empty'
    find_all_related_parcels(
        companies_ids=companies_ids,
        land_parcels=input_values_parcels,
        storage_parcels=storage_parcels
    )
    assert storage_parcels == expected, f'{storage_parcels} != {expected}'


@pytest.mark.end_to_end
@pytest.mark.positive
@pytest.mark.parametrize('company_id, expected', [
    ('c1', ['l1', 'l3', 'l4', 'l5']),
    ('c2', ['l2']),
    ('c3', ['l3', 'l4', 'l5']),
    ('c4', []),
    ('c5', ['l4', 'l5']),
    ('c6', []),
])
def test_get_land_parcels_for_company(company_id, expected, input_values_companies, input_values_parcels):
    assert isinstance(company_id, str), f"expect {type(str)}, received: {type(company_id)}"
    assert isinstance(input_values_companies, list), f"expect {type(list)}, received: {type(input_values_companies)}"
    assert isinstance(input_values_parcels, list), f"expect {type(list)}, received: {type(input_values_parcels)}"
    result = get_land_parcels_for_company(
        company_id=company_id,
        companies=input_values_companies,
        parcels=input_values_parcels
    )
    assert result == expected, f'{result} != {expected}'
