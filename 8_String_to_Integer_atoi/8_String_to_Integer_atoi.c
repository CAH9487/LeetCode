#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>

int atoi(const char *s) {
  int idx = 0;
  int result = 0;
  bool neg = false;

  while (s[idx] != '\0') {
    char c = s[idx++];
    if (c == ' ') continue;
    if (result == 0 && !neg && c == '-') {
      neg = true;
      continue;
    }
    if (result == 0 && !neg && c == '+') continue;
    if (c < 0x30 || c > 0x39) break;

    if (result > 0 && neg) {
      result *= -1;
      neg = !neg;
    }

    if (result > INT_MAX / 10 ||
        (result == INT_MAX / 10 && ((int)(c - 0x30)) > 7)) {
      return INT_MAX;
    }
    if (result < INT_MIN / 10 ||
        (result == INT_MIN / 10 && ((int)(c - 0x30)) > 8)) {
      return INT_MIN;
    }

    result = result * 10 +
             ((result >= 0) ? (int)(c - 0x30) : (-1 * (int)(c - 0x30)));
  }

  return result;
}

int main(int argc, char *argv[]) {
  char s[1024] = {0};
  int result;

  strcpy(s, "42");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");
  
  strcpy(s, "+-12");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "-42");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "0");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "   -42");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "wbc -42");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "2147483647");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "3147483647");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "-91283472332");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "-2147483649");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  return 0;
}
