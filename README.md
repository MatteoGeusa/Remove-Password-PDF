# PDF Batch Decryptor

A lightweight Python utility to remove password protection from multiple PDF files simultaneously. This tool is designed for automation workflows where you have a collection of encrypted PDFs sharing the same password and you need to process them for further analysis or archiving.

## 🚀 Purpose
Manually unlocking dozens of PDFs is time-consuming. This script automates the "Decrypt and Save-As" process, ensuring that your data pipeline remains uninterrupted by encryption barriers.

## 🛠️ Requirements
- Python 3.6+

## ⚙️ Installation
1. Clone this repository:
    ```bash
    git clone [https://github.com/yourusername/pdf-batch-decryptor.git](https://github.com/yourusername/pdf-batch-decryptor.git)
    ```
2. Install the required dependency:
    ```bash
    pip install -r .\requirements.txt
    ```

### 📂 Project Structure
data/: Place your password-protected PDF files here.

output/: The decrypted, "open" versions will be saved here automatically.

main.py: The core logic script.

### 💻 Usage
Place all your encrypted PDFs in the data folder.

Create an .env file cloning the .env.example content, replace "password_for_pdf_unlock" with the actual password of the files.

Run the script:

    ```Bash
    python main.py
    ```

### ⚠️ Disclaimer
This tool is intended for use with files where the user already knows the password. It is a management utility, not a decryption or "cracking" tool. Use responsibly and in accordance with local data privacy laws.