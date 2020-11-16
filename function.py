def bil_genap(item) :
    alist = []
    for i in item :
        if i % 2 == 0 :
            alist.append(i)
    return alist

angka = [1,2,3,4,5,6,7,8,9,10]

print("Sample : ",angka)
print("Angka : ",bil_genap(angka))