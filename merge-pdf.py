from PyPDF2 import PdfFileMerger

# Funzione di merging dei pdf
def merge_pdf_files(file_names, output_name):
    merger = PdfFileMerger()

    try:
        # Unisci i file PDF
        for file_name in file_names:
            merger.append(file_name)

        # Salva il file di output
        merger.write(output_name)
        print("I file sono stati uniti correttamente.")

    except Exception as e:
        print(f"Si è verificato un errore durante la fusione dei file: {e}")

    finally:
        merger.close()


# Input dei dati dall'utente
num_files = int(input("Inserisci il numero di file PDF da unire: "))
file_names = []
for i in range(num_files):
    file_name = input(f"Inserisci il nome del file PDF {i+1}: ")
    file_names.append(file_name)

output_name = input("Inserisci il nome del file di output: ")

# Unisci i file PDF
merge_pdf_files(file_names, output_name)

# Viene definita una funzione merge_pdf_files che accetta una lista di nomi di file PDF da unire e il nome del file di output desiderato.
# La funzione utilizza la libreria PyPDF2 per unire i file PDF specificati e salva il risultato nel file di output.
# All'utente viene quindi richiesto di inserire il numero di file PDF da unire e i loro nomi.
# Successivamente, viene chiesto di inserire il nome del file di output desiderato.
# Infine, viene chiamata la funzione merge_pdf_files con i dati inseriti dall'utente per unire i file PDF specificati.
# Assicurati di aver installato la libreria PyPDF2 utilizzando il comando pip install PyPDF2 prima di eseguire il codice.
