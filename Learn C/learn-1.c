#include <stdio.h>

int main(){
    int i = 0;
    for(;;){
        
        printf("%d ", i);
        i+=1;

        if (i>10){
            break;
        }
        
    }
    return 0;
}
