#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define max(a, b)           \
  ({                        \
    __typeof__(a) _a = (a); \
    __typeof__(b) _b = (b); \
    _a > _b ? _a : _b;      \
  })

#define min(a, b)           \
  ({                        \
    __typeof__(a) _a = (a); \
    __typeof__(b) _b = (b); \
    _a < _b ? _a : _b;      \
  })

// Brute Force Approach
// Runtime: 1072 ms, faster than 5.61% of C online submissions
// Memory Usage: 5.6 MB, less than 62.14% of C online submissions
int check_palindrome(char *s) {
  int len = strlen(s);
  int mid = (len + 1) / 2;
  int flag = 1;
  int i, j;
  if (len <= 1) return flag;
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

// Dynamic Programming Approach
// Runtime: 444 ms, faster than 10.44% of C online submissions
// Memory Usage: 181.6 MB, less than 5.13% of C online submissions
char *longestPalindrome_DP(char *s) {
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
      if (begin == end) continue;
      if ((end - 1) < (begin + 1)) {
        if (s[begin] == s[end]) {
          table[begin][end] = 2;
          table[end][begin] = true;  // s[begin:end] is palindrome
          strncpy(result, &s[begin], end - begin + 1);
          result[end - begin + 1] = '\0';
        } else {
          table[begin][end] = 1;
        }
        continue;
      }
      if (s[begin] == s[end] && table[end - 1][begin + 1]) {
        table[begin][end] = table[begin + 1][end - 1] + 2;
        table[end][begin] = true;  // s[begin:end] is palindrome
        strncpy(result, &s[begin], end - begin + 1);
        result[end - begin + 1] = '\0';
      } else {
        table[begin][end] = table[begin + 1][end - 1];
      }
    }
  }
  // dump_table(table, len);
  return result;
}

// Manacher Approach
// Runtime: 4 ms, faster than 95.54% of C online submissions for Longest Palindromic Substring.
// Memory Usage: 7.9 MB, less than 13.57% of C online submissions for Longest Palindromic Substring.
char *longestPalindrome(char *s) {
  int len = strlen(s);
  int nMax = 1;
  int pos = 0;
  int max_right = -1;
  char *ss = (char *)malloc(((len << 1) + 2) * sizeof(char));
  char *max_s = (char *)malloc((len + 1) * sizeof(char));
  int *p = (int *)malloc(((len << 1) + 1) * sizeof(int));
  memset(p, 0, (len << 1) * sizeof(char));
  if (len <= 1) {
    strcpy(ss, s);
    return ss;
  }

  ss[0] = '#';
  for (int i = 0; i < len; i++) {
    ss[(i << 1) + 1] = s[i];
    ss[(i << 1) + 2] = '#';
  }
  len = (len << 1) + 1;
  ss[len] = '\0';

  for (int i = 0; i < len; i++) {
    if (i < max_right) {
      p[i] = min(p[(pos << 1) - i], max_right - i);
    } else {
      p[i] = 1;
    }
    while (i - p[i] >= 0 && i + p[i] < len && ss[i - p[i]] == ss[i + p[i]])
      p[i]++;
    if (i + p[i] > max_right) {
      pos = i;
      max_right = i + p[i];
    }
    nMax = max(nMax, p[i] - 1);
  }

  // get result string
  int max_idx = -1;
  for (int i = 0; i < len; i++) {
    if (p[i] == nMax + 1) {
      max_idx = i;
      break;
    }
  }
  int idx = 0;
  for (int i = (max_idx - nMax); i < (max_idx + nMax); i++) {
    if (ss[i] == '#') continue;
    max_s[idx++] = ss[i];
  }
  max_s[idx] = '\0';

  return strdup(max_s);
}

int main(int argc, char *argv[]) {
  char s[1024] = {0};
  char *result = NULL;
  strcpy(s, "");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);

  strcpy(s, "a");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);

  strcpy(s, "ac");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);

  strcpy(s, "abcda");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);

  strcpy(s, "aba");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);

  strcpy(s, "babad");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);

  strcpy(s, "cbbd");
  result = longestPalindrome(s);
  printf("[%s], [%s]\n\n", s, result);
  free(result);
  return 0;
}
