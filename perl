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
TeOS/
├─ system/
│   ├─ kernel/
│   │   ├─ main.c          # Gerçek kernel başlangıcı
│   │   ├─ apps.c          # Tüm uygulamalar ve launch_app()
│   │   ├─ menu.c          # Ana menü ve fare tıklama
│   │   ├─ mouse.c         # Fare sürücüsü
│   │   └─ keyboard.c      # Klavye sürücüsü
│   ├─ boot/
│   │   └─ grub.cfg        # Bootloader GRUB
│   └─ config.h            # OS konfigürasyonu
├─ apps/                   # Gerçek uygulama kaynakları
│   ├─ Takky/
│   │   └─ main.c          # Takky oyunu
│   ├─ TeNotePRO/
│   │   └─ main.c
│   ├─ TeStore/
│   │   └─ main.c
│   ├─ TeClock/
│   ├─ TeCalendar/
│   ├─ TeWallpaper/
│   ├─ TeSecurity/
│   ├─ TeLearning/
│   ├─ TEDEV/
│   └─ TPKCreator/
├─ resources/              # Logo, animasyon, sesler
├─ data/                   # Kullanıcı verileri (tpk, ayarlar)
├─ manpages/               # Kullanıcı ve geliştirici kılavuzları
│   └─ TeOS.1.roff
├─ example/                # Örnek uygulamalar
│   └─ TakkyDemo/
│       └─ main.c
├─ log/                    # Derleme/test logları (gitignore ile hariç tutulur)
├─ cmd/                    # CLI araçları
│   └─ TeUpdate/
│       └─ main.c
├─ .gitignore              # Gereksiz dosyaları hariç tutar
├─ .github/
│   └─ workflows/
│       └─ build.yml       # Otomatik build CI
├─ go.mod                  # Go modülü (varsa Go uygulamaları için)
├─ go.sum                  # Go bağımlılıkları
└─ goreleaser.yml          # Otomatik release ve paketleme
