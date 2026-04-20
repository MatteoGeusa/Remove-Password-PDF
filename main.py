import os
from pypdf import PdfReader, PdfWriter
import dotenv

dotenv.load_dotenv()

def batch_unlock_pdfs(input_folder, output_folder, password):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Cartella '{output_folder}' creata.")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            try:
                reader = PdfReader(input_path)
                
                if reader.is_encrypted:
                    reader.decrypt(password)
                
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                
                with open(output_path, "wb") as f:
                    writer.write(f)
                
                print(f"Sbloccato con successo: {filename}")
                
            except Exception as e:
                print(f"Errore durante l'elaborazione di {filename}: {e}")

# Esecuzione del processo
batch_unlock_pdfs("data", "output", os.getenv('PASSW'))