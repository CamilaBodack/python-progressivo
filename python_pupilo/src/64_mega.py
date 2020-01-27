
dez_1 = 0
dez_2 = 0
dez_3 = 0
dez_4 = 0
dez_5 = 0
dez_6 = 0

dez_1 < dez_2 < dez_3 < dez_4 < dez_5 < dez_6

count = 0

for dez_1 in range(60):
    for dez_2 in range(dez_1+1,60):
        for dez_3 in range(dez_2+1,60):
            for dez_4 in range(dez_3+1,60):
                for dez_5 in range(dez_4+1,60):
                    for dez_6 in range(dez_5+1,60):
                        count += 1
print(count)


