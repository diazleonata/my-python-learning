data_mhs = {"12345": {"nama": "Budi", "prodi": "55201"}, 
            "54321": {"nama": "Joko", "prodi": "55202"}},

data_prodi = {"55201": "Informatika", "55202": "Sistem Informasi"}

data_makul = {"IF001": {"namaMk": "Pendidikan Pancasila", "sks": 3}, 
              "IF002": {"namaMk": "Pendidikan Agama", "sks": 2}}

data_nilai = {"12345": {"IF001": ["A"], "IF002": ["B"]}, 
              "54321": {"IF001": ["C"], "IF002": ["D"]}}

input_nim = input("Masukkan NIM: ")
nim_cari = data_mhs.get(input_nim)
nilai_cari = data_nilai.get(input_nim)

if nim_cari is not None:
    nama_prodi = data_mhs.get(input_nim)["prodi"]
    print(f"NIM : {input_nim}\nNama: {nim_cari['nama']}\nProdi: {nama_prodi}")
    if nilai_cari is not None:
        print("--------------------------------------------")
        print("No.\tKode MK\tNama MK\t\tSKS\tNHT\tNA\t\tTotal")
        no = 1
        totsks = 0
        totna = 0

        for kdmk, nilai in nilai_cari.items():
            makul_cari = data_makul.get(kdmk)
            if nilai[0] == 'A':
                na = 4
            elif nilai[0] == 'B':
                na = 3
            elif nilai[0] == 'C':
                na = 2
            elif nilai[0] == 'D':
                na = 1
            else:
                na = 0

            tot = makul_cari['sks'] * na
            totsks += makul_cari['sks']
            totna += tot
            print(f"{no}\t{kdmak}\t{makul_cari['namaMk']}\t{makul_cari['sks']}\t{nilai[0]}\t{na}\t{tot}")

            no += 1
        print("--------------------------------------------")
        print(f"Total SKS {totsks}")
        print(f"Total nilai {totna}")
        print(f"IPK {round(totna/totsks, 2)}")
    else:
        print("Data nilai tidak ada")
else:
    print("Nim yang dicari tidak ada")
