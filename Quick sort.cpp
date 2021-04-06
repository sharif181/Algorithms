#include<stdio.h>
void swap(int *a,int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int partition(int ar[],int left,int right)
{
    int pivot=ar[left];
    while(left<=right)
    {
        if(ar[left]==pivot)
        {
            if(pivot<ar[right])
                right--;
            else
            {
                swap(&ar[left],&ar[right]);
                pivot=ar[right];
                left++;
            }
        }
        else if(ar[right]==pivot)
        {
            if(ar[left]<pivot)
                left++;
            else
            {
                swap(&ar[left],&ar[right]);
                pivot=ar[left];
                right--;
            }
        }
    }
    return left;
}

void quickSort(int ar[],int left,int right)
{
    while(left<right)
    {
        int p=partition(ar,left,right);
        quickSort(ar,left,p-1);
        quickSort(ar,p+1,right);
    }

}
int main()
{
    int ar[]={2,1,9,4,5};
    quickSort(ar,0,4);
    int i;
    for(i=0;i<5;i++)
        printf("%d ",ar[i]);
}
