// keyboard_map.c — TeOS özel klavye düzeni

#include "keyboard_map.h"

char te_keymap[128] = {
    0,  27, // ESC
    '8', 'b', ':', '?', '3', 'f', '@', '#', // A–H
    '1', '!', '(', ')', ',', '.', '0', '+', // I–P
    '?', '4', '5', '7', '2', 'v', 'w', 'x', 'y', 'z', // Q–Z
    ' ', '\n', // Space, Enter
};

// Özel kısayollar:
void handle_te_shortcuts(unsigned char key) {
    switch (key) {
        case 20: // Ctrl+T → TeMenu
            printf("[TeOS] Ana Menü Açılıyor...\n");
            break;
        case 17: // Ctrl+Q → Uygulamayı kapat
            printf("[TeOS] Uygulama Kapatılıyor...\n");
            break;
        default:
            break;
    }
}
#ifndef TE_KEYBOARD_MAP_H
#define TE_KEYBOARD_MAP_H

#include <stdio.h>

extern char te_keymap[128];
void handle_te_shortcuts(unsigned char key);

#endif

#include "keyboard_map.h"

void keyboard_input(unsigned char keycode) {
    char key = te_keymap[keycode];
    handle_te_shortcuts(keycode);
    printf("%c", key);
}
