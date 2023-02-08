def allocate_resources(students, resources):
    students.sort(key=lambda x: x.priority, reverse=True)
