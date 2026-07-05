/*
 
1. 알고리즘 : 버블 정렬 알고리즘

2. 설명 : 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내는 알고리즘

3. 시간 복잡도 : O(N^2)
 
*/

#include <stdio.h>

int main(void) {

    int i, j, temp;

    int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

    for(i = 0; i < 10; i++) {
        for(j = 0; j < 9 - i; j++) {
            if(array[j] > array[j + 1]) {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }

        }

    }
    
    for(i = 0; i < 10; i++) {
        printf("%d ",array[i]);
    }
    
    return 0;

}