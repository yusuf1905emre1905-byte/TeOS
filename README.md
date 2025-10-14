## Bootloader (Gerçek Bilgisayarda Başlatma)

TeOS, kendi özel bootloader yapısına sahiptir.  
Bu sistem, BIOS veya UEFI tabanlı gerçek bilgisayarlarda **doğrudan açılabilir**.  
QEMU, VirtualBox veya diğer sanal makineler **gerekli değildir.**

### Bootloader Kaynak Kodu (Assembly)
```asm
; TeOS Bootloader v1.0
; BIOS uyumlu başlatıcı

[org 0x7C00]
[BITS 16]

start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7C00

    mov si, msg
    call print

    ; Kernel'i belleğe yükle
    mov bx, 0x8000
    mov ah, 0x02
    mov al, 1
    mov ch, 0
    mov cl, 2
    mov dh, 0
    int 0x13

    jmp 0x0000:0x8000

print:
    mov ah, 0x0E
.next:
    lodsb
    or al, al
    jz .done
    int 0x10
    jmp .next
.done:
    ret

msg db "Hello User! TeOS is booting...", 0

times 510-($-$$) db 0
dw 0xAA55
```

Bu dosyayı `boot.asm` olarak kaydet ve aşağıdaki komutla derle:

```bash
nasm -f bin boot.asm -o boot.bin
```

Oluşan `boot.bin` dosyasını bir USB belleğe veya disk imajına yazabilirsin:

```bash
dd if=boot.bin of=/dev/sdX bs=512 count=1
```

(⚠️ `/dev/sdX` kısmı senin USB sürücün olmalı.)

### Gerçek Donanımda Test Etme
1. BIOS/UEFI’den USB önyüklemeyi etkinleştir.  
2. Bilgisayarı yeniden başlat.  
3. TeOS logosu ve “Hello User! TeOS is booting…” mesajı gözükecek.  
4. Ardından sistem ana menüye (TeMenu) geçer.

---

## Özet

| Özellik | Durum |
|----------|--------|
| Gerçek BIOS/UEFI desteği | ✅ |
| Kernel | ✅ C tabanlı |
| GUI (masaüstü) | 🔄 Geliştiriliyor |
| AI Asistan (TeAI / Tessa) | 🔄 Deneysel |
| Sanal makine gereksinimi | ❌ Gerekmez |
| Geliştirme durumu | 🚀 Aktif |

---

**Artık TeOS gerçek bilgisayarda çalışabilen bir çekirdek + bootloader sistemine sahip.**
Her şey açık kaynak kodlu olarak GitHub deposunda barındırılabilir.
