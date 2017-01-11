import collections

# @include
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))


def sort_by_gpa(students):
    students.sort(key=lambda student: student.grade_point_average)


def sort_by_name(students):
    students[:] = sorted(students, key=lambda student: student.name)


# @exclude


def main():
    students = [
        Student('A', 4.0), Student('C', 3.0), Student('B', 2.0), Student('D',
                                                                         3.2)
    ]
    sort_by_gpa(students)
    assert all(
        students[i].grade_point_average <= students[i + 1].grade_point_average
        for i in range(len(students) - 1))
    sort_by_name(students)
    assert all(students[i].name <= students[i + 1].name
               for i in range(len(students) - 1))


if __name__ == '__main__':
    main()
