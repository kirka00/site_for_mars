from requests import get, post, delete


print(get('http://localhost:5000//api/v2/jobs').json())
print(get('http://localhost:5000//api/v2/qwerty').json())
print(get('http://localhost:5000/api/v2/1').json())
print(get('http://localhost:5000/api/v2/999').json())

print(delete('http://localhost:5000/api/jobs').json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())
print(delete('http://localhost:5000/api/v2/jobs/999').json())
print(delete('http://localhost:5000/api/v2/jobs/q').json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'name': 'Кухарка'}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'age': 67}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 4,
                 'job': 'enginer',
                 'work_size': 12,
                 'collaborators': '1, 2, 4',
                 'is_finished': False}).json())
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 2,
                 'job': 'ecologist',
                 'work_size': 10,
                 'collaborators': '3, 4, 5',
                 'is_finished': False}).json())