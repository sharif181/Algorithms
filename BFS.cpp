#include<bits/stdc++.h>

using namespace std;


vector<int> v[10];
int level[10];
bool vis[10];


void bfs(int s)
{
    queue <int> q;
    q.push(s);
    level[ s ] = 0 ;
    vis[ s ] = true;
    while(!q.empty())
    {
        int p = q.front();
        cout<<p<<endl;
        q.pop();
        for(int i = 0; i < v[p].size() ; i++)
        {
                if(vis[ v[ p ][ i ] ] == false)
                {
                    level[ v[ p ][ i ] ] = level[ p ]+1;
                    q.push(v[p][i]);
                    vis[ v[ p ][ i ] ] = true;
                }
        }
    }
}


int main()
{

    int i,a,b;

    int node,edge,source;
    for(i=0; i<7; i++)
    {
        cin>>a>>b;
        v[a].push_back(b);
    }

    for(i=0;i<node;i++)
        level[i]=0;
    for(i=0;i<node;i++)
        vis[i]=false;
    bfs(8);

    return 0;
}
