#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,q,r;
    cin>>a>>b;
    while(r!=0)
    {
        r=b%a;
        b=a;
        a=r;

    }
    printf("%d ",b);
    return 0;
}
