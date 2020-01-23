city_a_ano = 80000 + (80000*0.03)
city_b_ano = 200000 +(200000*0.015)
count = 0

while city_a_ano <= city_b_ano:
    city_a_ano = city_a_ano + (city_a_ano*0.03)
    city_b_ano = city_b_ano + (city_b_ano*0.015)
    count += 1
    print(count)

