#include <bits/stdc++.h>
using namespace std;

int TRS(int l,int r,int key,int ar[])
{
    if(r>=l){
    int mid1 = l+(r-l)/3;
    int mid2 = r-(r-l)/3;

    if(ar[mid1]==key) return 1;
    if(ar[mid2]==key) return 1;

    if(key<ar[mid1]) return TRS(l,mid1-1,key,ar);
    else if(key>ar[mid2]) return TRS(mid2+1,r,key,ar);
    else return TRS(mid1+1,mid2-1,key,ar);
    }
    return -1;
}

int main()
{
    int ar[]={1,2,3,4,5,6,7,8,9,10};
    int res = TRS(0,9,11,ar);
    if (res == 1) cout<<"Found"<<endl;
    else cout<<"Not Found"<<endl;
    return 0;
}
