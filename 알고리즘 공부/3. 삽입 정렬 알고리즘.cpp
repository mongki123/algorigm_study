/*
 
1. 알고리즘 : 삽입 정렬 알고리즘

2. 설명 : 각 숫자를 적절한 위치에 삽입하는 알고리즘
        
        // "거의 정렬된" 배열에는 어떤 정렬보다도 빠름
        // ex) {2, 3, 4, 5, 6, 6, 7, 8, 9, 1};

3. 시간 복잡도 : O(N^2)
 
*/

#include <stdio.h>

int main(void) {

    int i, j, temp;
    int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

    for(i = 0; i < 9; i++){
        j = i;
        while(array[j] > array[j+1] && (j>-0)) {
            temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
            if(j>0) j--;
        }
    }

    for(i = 0; i < 10; i++) {
        printf("%d ",array[i]);
    }


    return 0;
}