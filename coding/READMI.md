# Task 

### The Problem:
> We would like you to change the below function to return which land parcels the given company owns (__directly and indirectly__). <br>
> When you are ready, please open any text-editor/IDE you wish, paste the code below, and share your screen so we can collaborate on the solution. <br>
> _Don't forget you can ask as many questions as you want._
 
### Input data:
```python
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
```
