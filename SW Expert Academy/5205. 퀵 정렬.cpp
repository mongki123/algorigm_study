#include <stdio.h>

void quickSort(int *arr, int start, int end) {

    if(start >= end) {
        return;
    }

    int key = start;
    int i = start + 1;
    int j = end;
    int temp;

    while(i <= j) {

        while(arr[i] <= arr[key] && i <= end) {
            i++;
        } 
        while(arr[j] >= arr[key] && j > start) {
            j--;
        }
        if(i >= j) {
            temp = arr[key];
            arr[key] = arr[j];
            arr[j] = temp;
        } else {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        } 
    }

    quickSort(arr, start, j - 1);
    quickSort(arr, j + 1, end);
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        int number;
        scanf("%d",&number);
        int arr[number] = {};
        
        for(int j = 0; j < number; j++) {
            scanf("%d", &arr[j]);
        }
        quickSort(arr, 0, number - 1);

        printf("#%d %d\n", i, arr[number/2]);
    }
}