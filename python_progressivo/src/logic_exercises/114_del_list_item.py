bands = []

while True:
    choice = int(input("1 - Add band \n"
                       "2 - Show favorites \n"
                       "3 - List length \n"
                       "4 - Change option \n"
                       "5 - Delete item"))
    if choice == 1:
        band = input("Insert band name:")
        bands.append(band)
    if choice == 2:
        print(bands)
    if choice == 3:
        print("List length: ", len(bands))
    if choice == 4:
        index_to_change = int(input("Insert index to change band name"))
        if index_to_change < len(bands):
            change_band_name_to = input("Inser new band name:")
            bands[index_to_change] = change_band_name_to
        else:
            print("Index does not exists")
    if choice == 5:
        index_to_delete = int(input("Insert index to change band name"))
        del bands[index_to_delete]
