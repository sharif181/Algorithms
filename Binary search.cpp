#include<stdio.h>
void sort(int a[],int n)
{
    int i,j,key;
    for(i=1;i<n;i++)
    {
        key=a[i];
        j=i-1;
        while(j>=0&&a[j]>key){
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=key;
    }
}
void search(int a[],int n,int k){
       int i, hi, lo, mid;
        sort(a,n);
        lo = 0;

        hi = k-1;
        mid = (lo + hi) / 2;
        while (lo <= hi) {
            if (a[mid] < k) {
                lo = mid + 1;
            } else if (a[mid] == k) {
                printf("found\n");
                return ;
            } else {
                hi = mid - 1;
            }
            mid = (lo + hi) / 2;
        }
        printf("Not found\n");
        return;


}
int main(){
  int a[]={1,2,5,4,3,50};

  search(a,sizeof(a)/sizeof(a[0]),50);

}
