#include<stdio.h>
#define INF 1000000

int min(int a,int b){
    if(a<=b) return a;
    else return b;
}

void requiredCoin(int coins[],int c[],int n){
       printf("Coins: ");
    while(1){

    printf("%d ",coins[c[n]]);
    n=n-coins[c[n]];

    if(n==0) return;
    }
}

int dp_coin_change(int total,int coins[],int n)
{
    int i,j;
    int t[total+1],c[total+1];
    t[0]=0;
    for(i=1;i<=total;i++)
        t[i]=INF;
    for(i=0;i<=total;i++)
        c[i]=-1;

    for(j=0;j<n;j++)
    {
        for(i=coins[j];i<=total;i++){
            int a=min(t[i],1+t[i-coins[j]]);
            if(a!=t[i]){
                t[i]=a;
                c[i]=j;
            }
        }
    }
    requiredCoin(coins,c,total);
    printf("\n");
//    for(i=0;i<=total;i++){
//        printf("%d ",t[i]);
//    }
//    printf("\n");
//    for(i=0;i<=total;i++){
//        printf("%d ",c[i]);
//    }
    return t[total];
}

int main(){
    int total,i,n;
    scanf("%d %d",&n,&total);
    int coins[n];
    for(i=0;i<n;i++)
        scanf("%d",&coins[i]);
    int res = dp_coin_change(total,coins,n);
    printf("\nresult = %d\n",res);
    //printf("%d",coins[-3]);
    return 0;
}
