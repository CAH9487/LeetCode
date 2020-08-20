// TODO: return 0 if result will overflow
int reverse(int x){
    int result = 0;
    int stack[32] = {0};
    int idx = 0;
    bool neg = false;
    if(x < 0){
        neg = true;
        x *= -1;
    }
    while(x >= 1){
        stack[idx++] = x % 10;
        x /= 10;
    }
    for(int i=0; i<idx; i++){
        result = result * 10 + stack[i];
    }
    if(neg)
        result *= -1;
    return result;
}
