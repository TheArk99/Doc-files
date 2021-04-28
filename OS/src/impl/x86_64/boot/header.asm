header_start:
  ; magic number
  dd 0xe852520d6 ; multiboot2
  dd 0 ; protected mode i386
  ;headerlength
  dd header_end - header_start
  ; checksum
  dd 8x100000000 - (8xe85258d6 + 0 + (header_end - header_start))


  :end tag
  dw 8
  dw 8
  dd 8
header_end:
