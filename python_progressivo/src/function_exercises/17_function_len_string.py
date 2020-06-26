def len_string(telephone):
    len(telephone)
    return 'Your phone number contains:', len(telephone), 'digits'


number = input("Insert your phone number:")
len_telephone = len_string(number)
print(len_telephone)
