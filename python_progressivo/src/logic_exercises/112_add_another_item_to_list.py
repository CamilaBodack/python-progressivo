bands = []

while True:
    choice = int(input("1 - add band \n 2 - Show favorites \n 3 - List length"))
    if choice == 1:
        band = input("Insert band name:")
        bands.append(band)
    if choice == 2:
        print(bands)
    if choice == 3:
        print("List length: ", len(bands))
