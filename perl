TeOS/
├─ system/
│   ├─ kernel/
│   │   ├─ main.c       # Gerçek kernel başlangıcı
│   │   ├─ apps.c       # Tüm uygulamalar ve launch_app()
│   │   ├─ menu.c       # Ana menü ve fare tıklama
│   │   ├─ mouse.c      # Fare sürücüsü
│   │   └─ keyboard.c   # Klavye sürücüsü
│   ├─ boot/
│   │   └─ grub.cfg     # Bootloader GRUB
│   └─ config.h         # OS konfigürasyonu
├─ apps/                # Gerçek uygulama kaynakları
│   ├─ Takky/
│   ├─ TeNotePRO/
│   ├─ TeStore/
│   └─ ...              # Tüm diğer uygulamalar
├─ resources/           # Logo, animasyon, sesler
├─ data/                # Kullanıcı verileri (tpklar, ayarlar)
├─ manpages/            # Kullanıcı ve geliştirici kılavuzları
├─ example/             # Örnek uygulamalar
├─ log/                 # Derleme/test logları
├─ .gitignore           # Gereksiz dosyaları hariç tut
└─ .github/
    └─ workflows/
        └─ build.yml    # Otomatik build CI
