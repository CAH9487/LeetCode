#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Runtime: 4 ms, faster than 85.24% of C online submissions
// Memory Usage: 6.8 MB, less than 33.21% of C online submissions
char *zigzag_conversion(const char *s, int numRows) {
  int len = strlen(s);
  char result[1024] = {0};
  int idx = 0;
  int interval = (numRows - 1) * 2;
  if (numRows <= 1) {
    return strdup(s);
  }
  for (int i = 0; i < numRows; i++) {
    int j = i;
    int itv_1, itv_2;
    itv_1 = interval - (i * 2);
    itv_1 = (itv_1 <= 0) ? interval : itv_1;
    itv_2 = interval - itv_1;
    while (j < len) {
      result[idx++] = s[j];
      j += itv_1;
      if (itv_2 != 0 && j < len) {
        result[idx++] = s[j];
        j += itv_2;
      }
    }
    // result[idx] = '\0';
    // printf("%d - %s\n", i, result);
  }
  result[idx] = '\0';
  return strdup(result);
}

int main(int argc, char *argv[]) {
  char s[1024] = {0};
  char e[1024] = {0};
  char *result = NULL;

  strcpy(s, "PAYPALISHIRING");
  strcpy(e, "PAHNAPLSIIGYIR");
  result = zigzag_conversion((const char *)s, 3);
  printf("Input : [%s]\n", s);
  printf("Expect: [%s]\n", e);
  printf("Output: [%s]\n", result);
  if (strcmp(e, result) != 0) {
    printf("---- X\n");
  }
  free(result);

  printf("===============================\n");
  strcpy(s, "PAYPALISHIRING");
  strcpy(e, "PAYPALISHIRING");
  result = zigzag_conversion((const char *)s, 1);
  printf("Input : [%s]\n", s);
  printf("Expect: [%s]\n", e);
  printf("Output: [%s]\n", result);
  if (strcmp(e, result) != 0) {
    printf("---- X\n");
  }
  free(result);

  printf("===============================\n");
  strcpy(s, "");
  strcpy(e, "");
  result = zigzag_conversion((const char *)s, 3);
  printf("Input : [%s]\n", s);
  printf("Expect: [%s]\n", e);
  printf("Output: [%s]\n", result);
  if (strcmp(e, result) != 0) {
    printf("---- X\n");
  }
  free(result);

  return 0;
}
