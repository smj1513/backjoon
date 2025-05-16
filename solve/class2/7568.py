N = int(input())

persons = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(len(persons)):
    person1 = persons[i]
    rating = 1
    for j in range(len(persons)):
        person2 = persons[j]
        if person1[0] < person2[0] and person1[1] < person2[1]:
            rating += 1

    print(rating, end=" ")
