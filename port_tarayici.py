import socket

def port_tarama(adres, port_araligi):
    print(f"Adres: {adres} ({min(port_araligi)}-{max(port_araligi)}) portları taranıyor...\n")

    bulunan_portlar = []  # Açık portları saklayacak liste

    for numara in port_araligi:
        tarayici = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tarayici.settimeout(1)  # Zaman aşımı süresi 1 saniye olarak ayarlandı

        try:
            if tarayici.connect_ex((adres, numara)) == 0:
                bulunan_portlar.append(numara)
        except socket.error as hata:
            print(f"Port {numara} hata oluşturdu: {hata}")
        finally:
            tarayici.close()

    if bulunan_portlar:
        print("\n🔓 Erişilebilir Portlar:")
        for numara in bulunan_portlar:
            print(f"  [+] {numara} Numaralı Port Açık")
    else:
        print("❌ Açık port bulunamadı.")

# Kullanıcıdan taranacak IP adresini al
hedef_adres = input("Hedef IP adresini girin: ")
port_listesi = range(1, 65535)  # Tüm kullanılabilir portları kapsayan aralık

# Port tarama fonksiyonunu çalıştır
port_tarama(hedef_adres, port_listesi)
