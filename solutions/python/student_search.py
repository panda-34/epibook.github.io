import collections


# @include
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def search_student(students, target):
    return -1


# @exclude


def main():
    students = [Student('A', 4.0), Student('C', 3.0), Student('B', 2.0), Student('D', 3.2)]


if __name__ == '__main__':
    main()
