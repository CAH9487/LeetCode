#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Brute Force Approach
// Runtime: 1072 ms, faster than 5.61% of C online submissions for Longest
// Palindromic Substring.
// Memory Usage: 5.6 MB, less than 62.14% of C online submissions for Longest
// Palindromic Substring.
int check_palindrome(char *s) {
  int len = strlen(s);
  int mid = (len + 1) / 2;
  int flag = 1;
  int i, j;
  if (len <= 1)
    return flag;
  for (i = 0, j = len - 1; i < mid && j > 0; i++, j--) {
    if (s[i] != s[j]) {
      flag = 0;
      return flag;
    }
  }
  return flag;
}

char *longestPalindrome_BruteForce(char *s) {
  int len = strlen(s);
  char *result = (char *)malloc(1024 * sizeof(char));
  result[0] = '\0';

  for (int i = len; i > 0; i--) {
    for (int j = 0; j + i <= len; j++) {
      result[0] = '\0';
      strncpy(result, &s[j], i);
      result[j + i] = '\0';
      if (check_palindrome(result)) {
        return result;
      }
    }
  }
  return result;
}

void dump_table(int *table[], int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      printf("%3d, ", table[i][j]);
    }
    printf("\n");
  }
}

char *longestPalindrome(char *s) {
  int len = strlen(s);
  int **table = NULL;
  int begin, end;
  char *result = (char *)malloc(1024 * sizeof(char));
  result[0] = '\0';
  if (len <= 1) {
    strcpy(result, s);
    return result;
  }
  strncpy(result, s, 1);
  result[1] = '\0';
  table = (int **)malloc(len * sizeof(int *));
  for (int i = 0; i < len; i++) {
    table[i] = (int *)malloc(len * sizeof(int));
    memset(table[i], 0, len * sizeof(int));
    table[i][i] = 1;
  }

  for (int i = 1; i < len + 1; i++) {
    for (int begin = 0; begin + i <= len; begin++) {
      end = begin + i - 1;
      if (begin == end)
        continue;
      if ((end - 1) < (begin + 1)) {
        if (s[begin] == s[end]) {
          table[begin][end] = 2;
          strncpy(result, &s[begin], end - begin + 1);
          result[end - begin + 1] = '\0';
        } else {
          table[begin][end] = 1;
        }
        continue;
      }
      if (s[begin] == s[end]) {
        table[begin][end] = table[begin + 1][end - 1] + 2;
        strncpy(result, &s[begin], end - begin + 1);
        result[end - begin + 1] = '\0';
      } else {
        table[begin][end] = table[begin + 1][end - 1];
      }
    }
  }
  dump_table(table, len);
  return result;
}

int main(int argc, char *argv[]) {
  char s[1024] = {0};
  char *result = NULL;
  strcpy(s, "");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);

  strcpy(s, "a");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);

  strcpy(s, "ac");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);

  strcpy(s, "abcda");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);

  strcpy(s, "aba");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);

  strcpy(s, "babad");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);

  strcpy(s, "cbbd");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n", s, result);
  free(result);
  return 0;
}

