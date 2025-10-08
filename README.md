# TeOS
TeOS – Gerçek PC’de çalışan bootable işletim sistemi
# TeOS

TeOS, gerçek çalışan bir işletim sistemidir.  
Ana menüde tüm uygulamalar tıklanabilir ve fare/klavye ile kontrol edilebilir.  

## Özellikler
- Kernel + Ana Menü
- Tüm uygulamalar: Takky, TeNotePRO, TeStore, TEDEV, TPKCreator, TeGames, TeLearning, TeClock, TeCalendar, TeWallpaper, TeSecurity, TeEmail
- Fare ve Klavye desteği
- Kalıcı veriler (TPK, ayarlar)
- Bootable ISO üretimi

## Gereksinimler
- Linux/macOS terminal veya WSL (Windows)
- i686-elf-gcc ve i686-elf-ld
- GRUB ve grub-mkrescue
- (Opsiyonel) VirtualBox veya QEMU test için
Dikkat: ISO gerçek PC’de de çalışır, QEMU/VirtualBox kullanmak zorunlu değildir.

## Kurulum ve Derleme

```bash
# Repo klonla
git clone https://github.com/username/TeOS.git
cd TeOS

# Kernel derle
cd system/kernel
i686-elf-gcc -ffreestanding -c main.c -o main.o
i686-elf-ld -Ttext 0x1000 -o kernel.bin main.o --oformat binary

# ISO oluştur
mkdir -p isodir/boot/grub
cp kernel.bin isodir/boot/
cp boot/grub.cfg isodir/boot/grub/
grub-mkrescue -o TeOS.iso isodir

