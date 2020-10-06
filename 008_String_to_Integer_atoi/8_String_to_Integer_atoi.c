#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>

inline bool is_digit(const char c) { return (c >= 0x30 && c <= 0x39); }

// Runtime: 4 ms, faster than 55.89% of C online submissions
// Memory Usage: 5.6 MB, less than 15.43% of C online submissions
int atoi(const char *s) {
  int idx = 0;
  int result = 0;
  int neg = -1;
  bool have_digit = false;

  while (s[idx] != '\0') {
    char c = s[idx++];
    int d = (neg == 1) ? -1 * ((int)(c - 0x30)) : (int)(c - 0x30);
    if ((have_digit || neg >= 0) && !is_digit(c)) break;
    if (c == ' ') continue;
    if (result == 0 && neg == -1 && c == '-') {
      neg = 1;
      continue;
    }
    if (result == 0 && neg == -1 && c == '+') {
      neg = 0;
      continue;
    }
    if (!is_digit(c)) break;

    have_digit = true;

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

  strcpy(s, "9143 with words");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  strcpy(s, "-   123");
  result = atoi((const char *)s);
  printf("Input : [%s]\n", s);
  printf("Output: [%d]\n", result);
  printf("\n");

  return 0;
}
