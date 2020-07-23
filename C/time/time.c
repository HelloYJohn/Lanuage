#include <sys/time.h>
#include <stdio.h>

int main() {
  struct timeval tv;
  if (gettimeofday(&tv, NULL) == 0) {
    printf("%ld: \n", tv.tv_sec);
    printf("%ld: \n", tv.tv_usec);
  } else {
    printf("gettimeofday error");
  } 
  return 0;
}
