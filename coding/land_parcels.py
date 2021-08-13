# author: andrii budzan

def check_parent_id(company_id: str, company: dict) -> str:
    """ check if company_id is parent of company

    :param company_id: currently checking id
    :type company_id: str
    :param company: company, where we will check
    :type company: dict
    :return: company_id if related
    :rtype: str
    """
    if company.get('parentId', {}) == company_id:
        return company.get('id')


def find_all_related_companies(company_id: str, companies: list, storage: list) -> None:
    """ find all companies, related to company with id = company_id

    :param company_id: currently checking id
    :type company_id: str
    :param companies: list of companies to check
    :type companies: list
    :param storage: container to store related companies
    :type storage: list
    :return: -
    :rtype: None
    """
    if company_id not in storage:
        storage.append(company_id)
    for company in companies:
        if check_parent_id(company_id, company):
            storage.append(company.get('id'))
            find_all_related_companies(company.get('id'), companies, storage)


def check_parcels(company_id: str, parcel: dict) -> str:
    """ check if parcel related to company with id = company_id

    :param company_id: currently checking id
    :type company_id: str
    :param parcel: parcel to check
    :type parcel: dict
    :return: parcel id if matched
    :rtype:str
    """
    if parcel.get('companyId') == company_id:
        return parcel.get('id')


def find_all_related_parcels(companies_ids: list, land_parcels: list, storage_parcels: list) -> None:
    """ find all parcels, related to company with id = company_id

    :param companies_id: related companies
    :type companies_id: list
    :param land_parcels: land parcels
    :type land_parcels: list
    :param storage_parcels: container to store matched parcels ids
    :type storage_parcels: list
    :return: related parcels
    :rtype: list
    """
    for parcel in land_parcels:
        for company_id in companies_ids:
            if check_parcels(company_id, parcel):
                storage_parcels.append(parcel.get('id'))


# Implement the following function
#  E.g. get_land_parcels_for_company("c1") => ["l1","l3","l4","l5"]
def get_land_parcels_for_company(company_id: str, companies: list, parcels: list) -> list:
    """ get all parcels, that belongs to company with id = company_id directly and indirectly

    :param company_id: id to check
    :type company_id: str
    :param companies: all companies that must be checked
    :type companies: list
    :param parcels: all parcels that must be checked
    :type parcels: list
    :return: related parcels
    :rtype: list
    """
    related_companies = []
    related_parcels = []
    find_all_related_companies(
        company_id=company_id,
        companies=companies,
        storage=related_companies
    )
    find_all_related_parcels(
        companies_ids=related_companies,
        land_parcels=parcels,
        storage_parcels=related_parcels
    )
    return related_parcels


if __name__ == '__main__':
    from constants import companies, land_parcels
    company_id = 'c1'

    res = get_land_parcels_for_company(company_id=company_id, companies=companies, parcels=land_parcels)

    print(f'Company: | Related Parcels:')
    print(f'{company_id:>7} => {res}')
