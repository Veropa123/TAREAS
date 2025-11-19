import csv

def crear_csv(nombre, encabezados):
    with open(nombre, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(encabezados)

        

        