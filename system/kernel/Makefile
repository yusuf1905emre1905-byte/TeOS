# system/kernel/Makefile
CC = x86_64-elf-gcc
LD = x86_64-elf-ld
OBJCOPY = x86_64-elf-objcopy

CFLAGS = -std=gnu11 -ffreestanding -O2 -Wall -Wextra -fno-exceptions -fno-builtin
LDFLAGS = -nostdlib

SRCS = main.c
OBJS = $(SRCS:.c=.o)
OUT_ELF = kernel.elf
OUT_BIN = kernel.bin
LINKER = linker.ld

all: $(OUT_BIN)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(OUT_ELF): $(OBJS) $(LINKER)
	$(LD) -T $(LINKER) -o $(OUT_ELF) $(OBJS) $(LDFLAGS)

$(OUT_BIN): $(OUT_ELF)
	$(OBJCOPY) -O binary $(OUT_ELF) $(OUT_BIN)

clean:
	rm -f $(OBJS) $(OUT_ELF) $(OUT_BIN)
