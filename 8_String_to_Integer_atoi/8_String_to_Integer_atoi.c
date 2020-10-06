#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>

int atoi(const char *s) {
  int idx = 0;
  int result = 0;
  int neg = -1;

  while (s[idx] != '\0') {
    char c = s[idx++];
    int d = (neg == 1) ? -1 * ((int)(c - 0x30)) : (int)(c - 0x30);
    if (c == ' ') continue;
    if (result == 0 && neg == -1 && c == '-') {
      neg = 1;
      continue;
    }
    if (result == 0 && neg == -1 && c == '+') {
      neg = 0;
      continue;
    }
    if (c < 0x30 || c > 0x39) break;

    if (result > 0 && neg == 1) {
      result *= -1;
    }

    if (result > INT_MAX / 10 || (result == INT_MAX / 10 && d > 7)) {
      return INT_MAX;
    }
    if (result < INT_MIN / 10 || (result == INT_MIN / 10 && d < -8)) {
      return INT_MIN;
    }

    result = result * 10 + d;
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

  strcpy(s, "00000-42a1234");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  return 0;
}
