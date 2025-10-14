; === TeOS Bootloader ===
; Bu kod BIOS tarafından yüklendiğinde çalışır.
; Görev: "Hello User!" yazısını gösterip kernel'i başlatmak.

BITS 16
ORG 0x7C00              ; BIOS'un yükleme adresi

start:
    ; Ekranı temizle
    mov ax, 0x0600
    mov bh, 0x07
    mov cx, 0x0000
    mov dx, 0x184F
    int 0x10

    ; "Hello User!" yazısı
    mov si, msg
print_char:
    lodsb
    or al, al
    jz load_kernel
    mov ah, 0x0E
    int 0x10
    jmp print_char

load_kernel:
    ; Kernel'i diskin 2. sektöründen yükle
    mov ah, 0x02
    mov al, 5            ; 5 sektör oku (örnek)
    mov ch, 0x00
    mov cl, 0x02
    mov dh, 0x00
    mov dl, 0x80
    mov bx, 0x8000       ; RAM adresi
    int 0x13

    jmp 0x0000:0x8000    ; Kernel’e geçiş yap

msg db 'Hello User!', 0

times 510 - ($ - $$) db 0
dw 0xAA55               ; Boot imzası
