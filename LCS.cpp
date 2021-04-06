#include<bits/stdc++.h>
using namespace std;
char a[201],b[201];
int ar[300][300];
char br[300][300];
int n,m;
void print(int i,int j)
{
    if(i==0||j==0)
        return;
    else if(br[i][j]=='c')
    {
        print(i-1,j-1);
        printf("%c",a[i-1]);
    }
    else if(br[i][j]=='l')
        print(i,j-1);
    else
        print(i-1,j);
}
void lcs()
{
    int i,j;
    for(i=0;i<=n;i++)
    {
        for(j=0;j<=m;j++)
        {
            if(i==0||j==0)
                ar[i][j]=0;
            else if(a[i-1]==b[j-1])
            {
                ar[i][j]=ar[i-1][j-1]+1;
                br[i][j]='c';
            }
            else if(a[i-1]!=b[j-1])
            {
                if(ar[i][j-1]>ar[i-1][j])
                {
                    ar[i][j]=ar[i][j-1];
                    br[i][j]='l';
                }
                else
                {
                    ar[i][j]=ar[i-1][j];
                    br[i][j]='u';
                }
            }
        }
    }
    print(n,m);
    cout<<endl;
}
int main()
{
    int i,t;
    cin>>t;
    for(i=0;i<t;i++)
    {
    cin>>a;
    getchar();
    cin>>b;
    n=strlen(a);
    m=strlen(b);
    lcs();
    }

}
