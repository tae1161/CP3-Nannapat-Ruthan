def vatcalculate(totalpice):
    result = totalpice+(totalpice*7/100)
    return  result
x=int(input("Pice"))
print(vatcalculate(x))

