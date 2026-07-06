        barang_dapur = ["ikan", "ayam", "sayur", "daging"]
        tambahan = input("tambah barang : ")


        if tambahan.lower() in barang_dapur:
            print(f"{tambahan} dah ada, tak payah beli lagi.")

        else:
            print(f"Kena beli {tambahan} ni.")
            barang_dapur.append(tambahan.lower())

        print(f"Total ada {len(barang_dapur)} barang")