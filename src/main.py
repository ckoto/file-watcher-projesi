import time
import os
import sys


def auto_test():
    print("--- OTO TEST BASLIYOR ---")
    print("[TEST] Dosya sistemi kontrol ediliyor...")
    if os.path.exists("."):
        print("[BASARILI] Klasör erisimi var.")
    else:
        print("[HATA] Klasör yok!")
    print("--- OTO TEST BITTI ---")

# Programın ana kısmı
def main():
    # Eğer programı '--test' diye çalıştırırsan test moduna girer
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        auto_test()
        return

    print("Dosya Takipçisi Başladı... (Çıkmak için Ctrl+C)")
    path_to_watch = "."
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    
    while 1:
        time.sleep (2)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        
        if added: 
            print(f"[OLAY] Yeni dosya eklendi: {', '.join (added)}")
        if removed: 
            print(f"[OLAY] Dosya silindi: {', '.join (removed)}")
            
        before = after

if __name__ == "__main__":
    main()