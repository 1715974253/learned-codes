students = [{'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19},
            {'name': 'JACKZ', 'age': 22}]
# 关键字为name的升序排列
students.sort(key=lambda a:a['name'])
print(students)

# 关键字为age的降序排列
students.sort(key=lambda a:a['age'],reverse=True)
print(students)