kg = float(input("Berat anda : "))
m = float(input("Tinggi anda : "))

hasil = kg / m**2

if hasil <18.5:
    print("underweight")
elif hasil <25.0:
    print("normal weight")
elif hasil <30.0:
    print("overweight")
elif hasil >=30.0:
    print("obesity")