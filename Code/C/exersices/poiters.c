#include <stdio.h>

int main() {
  int n = 10;
  
  int * pointer = &n;
//  *pointer = *pointer + 1;

  if (pointer != &n) return 1;
  if (*pointer != 10) return 1;

  printf("done!\n");
  printf("this is what the pointer is %d\n",*pointer);
  printf("this is what the pointer is %d\n",pointer);
  return 0;
}
