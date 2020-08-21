int reverse(int x){
    int result = 0;
    int stack[32] = {0};
    int idx = 0;
    while(x != 0){
        stack[idx++] = x % 10;
        x /= 10;
    }
    for(int i=0; i<idx; i++){
        if(result > INT_MAX/10 || (result == INT_MAX/10 && stack[i] > 7) ||
           result < INT_MIN/10 || (result == INT_MIN/10  && stack[i] < -8))
            return 0;
        result = result * 10 + stack[i];
    }
    return result;
}