import os
import glob

def cleanup_jpg_files():
    jpg_files = glob.glob("*.jpg")
    if not jpg_files:
        print("[INFO] Nenhum arquivo .jpg para apagar.")
        return

    for file in jpg_files:
        try:
            os.remove(file)
            print(f"[INFO] Arquivo apagado: {file}")
        except Exception as e:
            print(f"[ERRO] Falha ao apagar arquivo {file}: {e}")
