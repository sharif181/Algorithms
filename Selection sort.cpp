#include<bits/stdc++.h>
using namespace std;
int main()
{
    int ar[]={3,4,1,0,-9};
    int i,j,l,Min,index;
    for(i=0;i<4;i++)
    {
        index=i;
        for(j=i+1;j<=4;j++)
        {
            if(ar[j]<ar[index]){
                index=j;
            }
        }
        swap(ar[i],ar[index]);

    }
    for(i=0;i<5;i++)
        cout<<ar[i]<<" ";
    return 0;
}
