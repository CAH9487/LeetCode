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

bool isMatch(const char *s, const char *p)
{
  int s_len = strlen(s);
  int p_len = strlen(p);
  char s_cur = '\0';
  char p_prev = '\0';
  char p_cur = '\0';
  int j = 0;
  if ((s_len == 0 || p_len == 0) && s_len != p_len)
    return false;
  if (s_len != p_len && !WD_in_string(p))
    return false;
  p_cur = p[0];
  if (isWD(p_cur))
    return false;
  for (int i = 0; s[i] && p_cur; i++)
  {
    if (isWD(p_prev) && isWD(p_cur))
      return false;
    s_cur = s[i];
    if (s_cur == p_cur)
    {
      p_prev = p_cur;
      p_cur = p[++j];
      continue;
    }
    else if (isDot(p_cur))
    {
      p_prev = p_cur;
      p_cur = p[++j];
      continue;
    }
    else if (isWD(p_cur))
    {
      if (s_cur == p_prev)
        continue;
      else if (isDot(p_prev))
        continue;
    }

  L_LABEL:
    p_prev = p_cur;
    p_cur = p[++j];
    if (isWD(p_prev) && isWD(p_cur))
      return false;
    if (s_cur == p_cur)
    {
      p_prev = p_cur;
      p_cur = p[++j];
      continue;
    }
    else if (isDot(p_cur))
    {
      p_prev = p_cur;
      p_cur = p[++j];
      continue;
    }
    else if (isWD(p_cur))
    {
      if (s_cur == p_prev)
        continue;
      else if (isDot(p_prev))
        continue;
      else
        goto L_LABEL;
    }
    else
      return false;
  }

  if (p_cur != '\0' && j < p_len - 1)
    return false;
  return true;
}

int main(int argc, char *argv[])
{
  char s[1024] = {0};
  char p[1024] = {0};
  bool result;

  strcpy(s, "aa");
  strcpy(p, "a");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aa");
  strcpy(p, "a*");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "ab");
  strcpy(p, ".*");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aab");
  strcpy(p, "c*a*b");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "mississippi");
  strcpy(p, "mis*is*p*.");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "mississippi");
  strcpy(p, "mis*is*ip*.");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aab");
  strcpy(p, "c*a**b");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aa");
  strcpy(p, "*a");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "ab");
  strcpy(p, ".*c");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, "aaaa");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, ".a");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aaa");
  strcpy(p, "a*a");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result ? "True" : "False");
  if (result != false)
    printf("----- X\n");
  printf("\n");

  return 0;
}
