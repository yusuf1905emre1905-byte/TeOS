#include <stdio.h>
#include "characters.c"
#include "mini_games.c"

void takky_run_init() {
    printf("Takky Run Modülü Başlatıldı!\n");
    show_character_status(Takky);
    show_character_status(Cubby);
    show_character_status(Doggy);
    show_character_status(Borty);

    // Mini oyunları sırayla başlat
    play_cubby_game();
    play_doggy_game();
    play_borty_game();
}
