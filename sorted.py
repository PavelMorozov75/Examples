student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
print(sorted(student_tuples, key=lambda student: student[2]))   # сортируем по возрасту
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

from operator import itemgetter, attrgetter, methodcaller

print(sorted(student_tuples, key=itemgetter(2)))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

