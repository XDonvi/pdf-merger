from PyPDF2 import PdfFileMerger

# Funzione di merging dei PDF
def merge_pdf_files(file_names, output_name):
    merger = PdfFileMerger()

    try:
        # Unisco i file PDF
        for file_name in file_names:
            merger.append(file_name)

        # Salvo il file di output
        merger.write(output_name)
        print("I file sono stati uniti correttamente.")

    except Exception as e:
        print(f"Si è verificato un errore durante la fusione dei file: {e}")

    finally:
        merger.close()


# Input dei dati utente
num_files = int(input("Inserisci il numero di file PDF da unire: "))
file_names = []

for i in range(num_files):
    file_name = input(f"Inserisci il nome del file PDF {i+1}: ")
    file_names.append(file_name)

output_name = input("Inserisci il nome del file di output: ")

# Richiamo la funzione di merginge dei PDF
merge_pdf_files(file_names, output_name)

