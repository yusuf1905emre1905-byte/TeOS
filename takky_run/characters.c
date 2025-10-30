#include <stdio.h>

typedef struct {
    char* name;
    int energy;
    int happiness;
    int hunger;
} Character;

Character Takky = {"Takky", 100, 100, 50};
Character Cubby = {"Cubby", 100, 100, 50};
Character Doggy = {"Doggy", 100, 100, 50};
Character Borty = {"Borty", 100, 100, 50};
Character Flamo = {"Flamo", 100, 100, 50};
Character Drippo = {"Drippo", 100, 100, 50};
Character Sparky = {"Sparky", 100, 100, 50};

void show_character_status(Character c) {
    printf("%s -> Energy: %d, Happiness: %d, Hunger: %d\n", c.name, c.energy, c.happiness, c.hunger);
}
