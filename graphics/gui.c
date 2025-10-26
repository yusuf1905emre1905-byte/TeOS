// === TeOS GUI Başlangıç Sistemi (grafik mod 13h) ===
// 320x200 çözünürlükte basit masaüstü görünümü + simgeler + saat

#include <stdint.h>

#define SCREEN ((uint8_t*)0xA0000)
#define WIDTH 320
#define HEIGHT 200

void putpixel(int x, int y, uint8_t color) {
    SCREEN[y * WIDTH + x] = color;
}

void draw_rect(int x, int y, int w, int h, uint8_t color) {
    for (int i = y; i < y + h; i++)
        for (int j = x; j < x + w; j++)
            putpixel(j, i, color);
}

void draw_icon(int x, int y, const char *label, uint8_t color) {
    draw_rect(x, y, 30, 30, color);
    char *v = (char*)0xB8000 + ((y / 8) + 22) * 160 + (x / 4);
    while (*label) {
        *v++ = *label++;
        *v++ = 0x0F;
    }
}

void set_video_mode(uint8_t mode) {
    asm volatile("int $0x10" : : "a"((0x00 << 8) | mode));
}

void draw_desktop() {
    // Arkaplan
    draw_rect(0, 0, WIDTH, HEIGHT, 1);

    // "Masaüstü simgeleri"
    draw_icon(20, 30, "AI", 4);        // TekonAI
    draw_icon(70, 30, "Files", 2);     // TeFiles
    draw_icon(120, 30, "Clock", 3);    // Saat
    draw_icon(170, 30, "Settings", 5); // Ayarlar

    // Üst menü çubuğu
    draw_rect(0, 0, WIDTH, 15, 8);
}

void show_clock() {
    // Şu an gerçek zaman yok (RTC bağlanmadı), ama örnek görüntü
    draw_rect(260, 3, 50, 10, 7);
    char *v = (char*)0xB8000 + (25 * 160) - 20;
    char *msg = "12:00";
    while (*msg) {
        *v++ = *msg++;
        *v++ = 0x0F;
    }
}

void gui_main() {
    set_video_mode(0x13); // 320x200 grafik mod
    draw_desktop();
    show_clock();
    for(;;); // GUI açık kalsın
}
