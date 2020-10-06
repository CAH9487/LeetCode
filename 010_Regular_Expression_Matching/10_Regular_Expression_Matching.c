#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isMatch(const char * s, const char * p){
    return true;
}


int main(int argc, char *argv[]) {
  char s[1024] = {0};
  char p[1024] = {0};
  bool result;

  strcpy(s, "aa");
  strcpy(p, "a");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result?"True":"False");
  if(result != false)
    printf("----- X\n");
  printf("\n");
  
  strcpy(s, "aa");
  strcpy(p, "a*");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result?"True":"False");
  if(result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "ab");
  strcpy(p, ".*");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result?"True":"False");
  if(result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "aab");
  strcpy(p, "c*a*b");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result?"True":"False");
  if(result != true)
    printf("----- X\n");
  printf("\n");

  strcpy(s, "mississippi");
  strcpy(p, "mis*is*p*.");
  result = isMatch((const char *)s, (const char *)p);
  printf("Input : s = [%s], p = [%s]\n", s, p);
  printf("Output: %s\n", result?"True":"False");
  if(result != false)
    printf("----- X\n");
  printf("\n");

  return 0;
}
