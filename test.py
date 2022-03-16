from requests import get, post, delete


print(get('http://localhost:5000//api/v2/users').json())
print(get('http://localhost:5000//api/v2/qwerty').json())
print(get('http://localhost:5000/api/v2/1').json())
print(get('http://localhost:5000/api/v2/999').json())

print(delete('http://localhost:5000/api/users').json())
print(delete('http://localhost:5000/api/v2/users/1').json())
print(delete('http://localhost:5000/api/v2/users/999').json())
print(delete('http://localhost:5000/api/v2/users/q').json())

print(post('http://localhost:5000/api/v2/users',
           json={'name': 'Кухарка'}).json())
print(post('http://localhost:5000/api/v2/users',
           json={'age': 67}).json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Kobzev',
                 'name': 'Kirill',
                 'age': 17,
                 'position': 'commander',
                 'speciality': 'enginer',
                 'address': 'module_123',
                 'email': 'kirkobzev@test.ru',
                 'hashed_password': '123QEFsdvzbvnhzBXckjadsbh!'}).json())
print(post('http://localhost:5000/api/jobs',
           json={'surname': 'Den',
                 'name': 'Serpuhov',
                 'age': 26,
                 'position': 'oficer',
                 'speciality': 'water enginer',
                 'address': 'module_12',
                 'email': 'den_ser@test.ru',
                 'hashed_password': 'isadfhisufdahuofsaiu!'}).json())