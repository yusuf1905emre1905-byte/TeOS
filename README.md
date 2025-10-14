# TeOS — The Experimental Operating System

TeOS, sıfırdan geliştirilen, hafif, hızlı ve modüler bir işletim sistemidir.  
Linux veya QEMU tabanlı değildir — doğrudan gerçek bilgisayarda çalışabilecek şekilde tasarlanmıştır.

## Özellikler

- Tamamen C ve Assembly ile yazılmış çekirdek (kernel)
- Gerçek donanım desteği (QEMU gerekmez — BIOS/UEFI ile çalışabilir)
- Modüler yapı:
  - TeStore (uygulama mağazası)
  - TeNotes, TeFiles, TeCamera, TeMusic, TeVideo
  - TeKids, TeWeather, TeLearning, TeDev
- Özel dosya biçimi: .TPK (TeOS Package)
- TeAI (Tessa) — sistem içi yapay zekâ asistanı
- Gerçek masaüstü arayüzü (grafik destekli sürüm hazırlıkta)

## Klasör Yapısı

```
TeOS/
├── kernel/
│   ├── main.c
│   ├── config.h
│   └── teos.cfg
│
├── system/
│   ├── init.c
│   └── users.cfg
│
├── gui/
│   ├── desktop.c
│   └── icons/
│
├── build/
│   ├── Makefile
│   └── build.sh
│
└── README.md
```

## Derleme (Gerçek Bilgisayarda)

TeOS, QEMU gerektirmeden normal bilgisayarda derlenip çalıştırılabilir.  
Sadece bir C derleyicisi (örneğin GCC) gereklidir.

```bash
gcc kernel/main.c -o teos
./teos
```

Bu komut, sistemi doğrudan terminalde başlatır.  
İstersen build.sh kullanarak otomatik derleme de yapabilirsin.

## Geliştirici Notu

TeOS halen erken geliştirme aşamasındadır.  
Ancak gerçek BIOS/UEFI uyumlu bir önyükleyici sürümü (bootloader) planlanmaktadır.  
Hedef, tamamen bağımsız bir işletim sistemi olarak kendi kernel’iyle açılabilmesidir.

## Lisans

MIT Lisansı altında sunulmaktadır.  
© 2025 TeOS Project Team
