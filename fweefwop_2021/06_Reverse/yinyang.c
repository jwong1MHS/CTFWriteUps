// Assume this runs on a 64-bit Linux
#include <stdio.h>
int main() {
   int i;
   scanf("%d", &i);
   i *= 3;
   if (i == -1) {
     printf("You are right!\n");
   } else {
     printf("Nay!\n");
   }

   return 0;
}
