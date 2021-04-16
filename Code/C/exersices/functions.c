#include <stdio.h>

int foo(int bar);

int main() {
  printf("%d", foo(4));
}

int foo(int bar) {
  return bar * 1;
}
