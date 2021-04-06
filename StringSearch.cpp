#include<stdio.h>
#include<string.h>

void search(char (*a)[20],char b[])
{
    int i,found=0;
    for(i=0;i<5;i++)
    {
       if(strcmp(a[i],b)==0)
        {
            found=1;
            break;
        }
    }
    if(found==1)
        printf("Found\n");
    else
        printf("not found\n");
}


int main()
{
    int found;
    char name[5][20];
    int i;
    printf("Enter 5 Strings : \n");
    for(i=0; i<5; i++)
    {
        gets(name[i]);
    }
    char want[20];
    printf("Which value you want to search?");
    gets(want);
        search(name,want);

//    for(i=0; i<5; i++)
//    {
//        if(strcmp(name[i],want)==0)
//        {
//            found=1;
//            break;
//        }
//    }
//    if(found==1)
//        printf("Found\n");
//    else
//        printf("Not found\n");

}
