/* system/kernel/main.c */
#include <stdint.h>

/* Multiboot header for GRUB (legacy multiboot) */
__attribute__((section(".multiboot"), used))
const uint32_t multiboot_header[] = {
    0x1BADB002,       /* magic */
    0x00000003,       /* flags: request memory info */
    -(0x1BADB002 + 0x00000003)
};

/* VGA text buffer */
volatile uint16_t *vga = (volatile uint16_t *)0xB8000;
const int VGA_WIDTH = 80;
const int VGA_HEIGHT = 25;

/* simple function to write string at row 0,col 0 */
static void kputs(const char *s) {
    int col = 0, row = 0;
    for (const char *p = s; *p; ++p) {
        if (*p == '\n') { row++; col = 0; continue; }
        if (col >= VGA_WIDTH) { col = 0; row++; }
        if (row >= VGA_HEIGHT) { /* scroll not implemented */ row = 0; }
        vga[row * VGA_WIDTH + col] = (uint16_t)((0x0F << 8) | (uint8_t)*p);
        col++;
    }
}

/* very small memory-set */
static void *kmemset(void *s, int c, unsigned long n) {
    unsigned char *p = s;
    while (n--) *p++ = (unsigned char)c;
    return s;
}

/* Kernel entry (called by multiboot) */
void kmain(void) {
    /* clear screen */
    for (int i = 0; i < VGA_WIDTH * VGA_HEIGHT; ++i) {
        vga[i] = (uint16_t)((0x0F << 8) | ' ');
    }

    kputs("Hello User!\n");
    kputs("TeOS booted.\n");
    kputs("Loading basic services...\n");

    /* placeholder for init: menu, drivers, etc. */
    while (1) {
        /* halt CPU until next interrupt to avoid 100% loop */
        __asm__ volatile ("hlt");
    }
}
