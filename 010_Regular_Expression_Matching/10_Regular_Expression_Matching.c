#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define SYM_DOT '.'
#define SYM_WD '*'

static inline bool isDot(const char c) { return c == SYM_DOT; }
static inline bool isWD(const char c) { return c == SYM_WD; }
static inline bool WD_in_string(const char *s)
{
  for (int i = 0; s[i]; i++)
  {
    if (isWD(s[i]))
      return true;
  }
  return false;
}

// Recursive Approach
// Runtime: 60 ms, faster than 16.59% of C online submissions
// Memory Usage: 5.4 MB, less than 35.87% of C online submissions
// https://ithelp.ithome.com.tw/articles/10213698
bool isMatch_Recursive(const char *s, const char *p)
{
  int s_len = strlen(s);
  int p_len = strlen(p);
  bool match = false;
  if (p_len == 0 && s_len == 0)
    return true;
  match = s_len > 0 && (s[0] == p[0] || isDot(p[0]));
  if (p_len >= 2 && isWD(p[1]))
    return isMatch_Recursive(s, &p[2]) || (match && isMatch_Recursive(&s[1], p));
  else
    return match && isMatch_Recursive(&s[1], &p[1]);
}

// DP Approach
bool isMatch_DP(const char *s, const char *p)
{
  return false;
}

int main(int argc, char *argv[])
{
  char s[1024] = {0};
  char p[1024] = {0};
  bool result;

  strcpy(s, "aa");
  strcpy(p, "a");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aa");
  strcpy(p, "a*");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "ab");
  strcpy(p, ".*");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aab");
  strcpy(p, "c*a*b");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "mississippi");
  strcpy(p, "mis*is*p*.");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "mississippi");
  strcpy(p, "mis*is*ip*.");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aab");
  strcpy(p, "c*a**b");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aa");
  strcpy(p, "*a");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "ab");
  strcpy(p, ".*c");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, "aaaa");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, ".a");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, "a*a");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, "ab*a");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, "ab*a*c*a");
  result = isMatch_DP((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  return 0;
}
