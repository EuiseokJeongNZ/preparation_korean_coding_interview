def solution(mats, park):
    answer = set()

    park_i = len(park)
    park_j = len(park[0])

    for mat in mats:
        for i in range(park_i):
            for j in range(park_j):
                if i + mat > park_i or j + mat > park_j:
                    continue
                    
                flag = True
                for mat_i in range(i, i + mat):
                    for mat_j in range(j, j + mat):
                        if park[mat_i][mat_j] != "-1":
                            flag = False
                            break

                    if not flag:
                        break

                if flag:
                    answer.add(mat)

    return max(answer) if answer else -1