bool isPalindrome(int x){
    int len = 0;
    int stack[32];
    int x_bk = x;
    int t;
    if(x < 0)
        return false;
    while(x != 0){
        t = x % 10;
        x /= 10;
        stack[len++] = t;
    }
    x = x_bk;
    while(x != 0){
        t = x % 10;
        x /= 10;
        if(t != stack[--len])
            return false;
    }
    return true;
}
