# author: andrii budzan

companies = [
    {"id": "c1", "name": "Big Corp A", "parentId": None},
    {"id": "c2", "name": "Big Corp B", "parentId": None},
    {"id": "c3", "name": "Medium Corp A", "parentId": "c1"},
    {"id": "c4", "name": "Medium Corp B", "parentId": "c2"},
    {"id": "c5", "name": "Small Corp A", "parentId": "c3"},
    {"id": "c6", "name": "Small Corp B", "parentId": "c3"},
]

land_parcels = [
    {"id": "l1", "companyId": "c1"},
    {"id": "l2", "companyId": "c2"},
    {"id": "l3", "companyId": "c3"},
    {"id": "l4", "companyId": "c5"},
    {"id": "l5", "companyId": "c5"},
]
