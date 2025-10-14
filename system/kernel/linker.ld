ENTRY(kmain)

SECTIONS
{
  /* place the kernel at 1MiB which is a common safe place */
  . = 0x00100000;

  .text :
  {
    *(.multiboot)
    *(.text*)
  }

  .rodata : { *(.rodata*) }

  .data : { *(.data*) }

  .bss :
  {
    __bss_start = .;
    *(.bss*)
    *(COMMON)
    __bss_end = .;
  }

  /DISCARD/ : { *(.eh_frame) }
}
