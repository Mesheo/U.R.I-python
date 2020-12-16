def createPlantation(lines):
    plantacao = []
    for i in range(lines):
        line = [int(y) for y in input().split()]
        plantacao.append(line)
    return plantacao

L, C, M, N = list(map(int, input().split()))
plantation = createPlantation(L)

sums = []
for plotH in range(L//M):
    for plotV in range(C//N):
        plotSum = 0
        for i in range(M):
            for j in range(N):
                plotSum += plantation[i + plotH][j + plotV]
        sums.append(plotSum)

print(max(sums))



