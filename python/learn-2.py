import prettytable
table = prettytable.PrettyTable()

presensi = float(input("Masukkan nilai presensi (0-100): "))
tugas = float(input("Masukkan nilai tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))

table.field_names = ["Presensi", "Tugas", "UTS", "UAS", "Nilai Akhir", "Nilai Huruf"]

for p, t, u, ua in zip(presensi, tugas, uts, uas):
    na = (10/100*p) + (30/100*t) + (30/100*u) + (30/100*ua)
    if na >= 80:
        nh = "A"
    elif na >= 70:
        nh = "B"
    elif na >= 50:
        nh = "C"
    elif na >= 30:             
        nh = "D"
    else:
        nh = "E"
    table.add_row([p, t, u, ua, na, nh])

print(table)    
