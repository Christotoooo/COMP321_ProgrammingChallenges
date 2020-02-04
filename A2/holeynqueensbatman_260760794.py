#include <stdio.h>
#include <string.h>


int absoluate_value(int x)
{return x < 0 ? -x : x;}


int attach(int r1, int c1, int r2, int c2)
{return c1==c2||r1==r2||absoluate_value(r1-r2)==absoluate_value(c1-c2) ? 1 : 0;}


int attach_pri(int* variables, int next_one){
    for (int p=0;p<next_one;p++){ if (attach(variables[next_one],next_one,variables[p],p)) return 1;}
    return 0;}



int conquer(int* variables, char* all_holes, int next_one, int n){
    if (next_one==n) return 1;
    int sum=0;

    for (int i=0; i<n; i++){
        variables[next_one]=i;
        
        if (all_holes[next_one+n*i]) continue;
        if (attach_pri(variables,next_one)) continue;
        
        sum = sum+conquer(variables,all_holes,next_one+1,n);}

    return sum;}


int output(int n, char* all_holes){
    // columns make up variables
    int variables[n]; 

    return conquer(variables, all_holes, 0, n);}


int main(){
    int n,h;
    char all_holes[144];
    while(1){
        scanf("%d %d", &n, &h);
        if (!n&&!h) break;

        memset(all_holes,0,144*sizeof(char));
        
        while(h--){
            int row,col;
            scanf("%d %d",&row,&col);
            all_holes[row*n+col]=1;}
        printf("%d\n", output(n, all_holes));}


    return 0;}