#include<bits/stdc++.h>
using namespace std;

int KanpScak(int S,int s[],int v[],int n)
{
    int V[n+1][S+1];
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=S;j++){
            if (i==0||j==0)
                V[i][j]=0;
            else
            {
                if(s[i-1]<=j)
                {
                    V[i][j]=max(v[i-1]+V[i-1][j-s[i-1]],V[i-1][j]);
                }
                else
                    V[i][j]=V[i-1][j];
            }
        }
    }
    return V[n][S];
}

int main()
{
//    int S=9,n=4;
//    int s[]={2,3,4,5};
//    int v[]={3,4,5,6};
        int S,n;
        cin>>S;
        cin>>n;
        int s[n],v[n];
        for (int i=0;i<n;i++) cin>>s[i];
        for (int i=0;i<n;i++) cin>>v[i];
    cout<<KanpScak(S,s,v,n);
}
