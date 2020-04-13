#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

using namespace std;


// initialization
int counter;  
int h, n, m;  
int number;

const int N = 1e3 + 100;

// cell_map stores the configuration of the bee's cells.
char cell_map[N][N];
int answer[N * N];
  


//odd case
const int cell_odd[6][2]={0, 1, 0, -1, 1, 0, -1, 0, -1, -1, 1, -1};
//even case
const int cell_even[6][2]={0, 1, 0, -1, 1, 0, -1, 0, 1, 1, -1, 1};



// helper function to compare two answers.
bool is_greater_than(int a,int b){
    return a > b;
}

// We use DFS to traverse the whole map.
void DFS(int x,int y){
	// we reach this point x,y so we fill this cell.
	cell_map[x][y]='#';
	// we increment the number of cells that we have traversed.
    number = number + 1;

    // we traverse along with six directions of a cell
    // note the difference between odd and even rows of cells. 
    for(int i = 0; i < 6; i++){
        
        int aa, bb;
        
        // odd case
        if(x&1){
            aa = cell_even[i][0] + x;
            bb = cell_even[i][1] + y;
        }// even case
        else{
            aa = cell_odd[i][0] + x;
            bb = cell_odd[i][1] + y;
        }
        
        // check if this cell is filled already.
        if(cell_map[aa][bb]=='#') continue;
        // or if a cell is out of range (no harm in this case) 
        if(aa<0 || aa>=n || bb<0 || bb>=m) continue;

        // we need to keep updating during the DFS.
        // if we pass all the checks, we head into DFS again starting at this cell.
        DFS(aa,bb);
    }
}

void output(){
	int temp = 0;
    int temp2 = 0;
    int c = 0;
    while(temp2 < h && c < counter){
        temp += 1;
        temp2 += answer[c];
        c += 1;
    }
    //output
    cout << temp << endl;  
}
  

  
  
int main(){
	// read the first line of three numbers.
    int unused_val = scanf("%d%d%d",&h,&n,&m);
    counter=0;

    getchar(); // important
    
    // read and store the whole configuration
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> cell_map[i][j];
        }
    }

    // traverse the whole configuration by looping and DFS
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(cell_map[i][j] == '.'){
            	// for each starting cell, we init a new number
            	// to store the number of cells traversed.
                number = 0;
                DFS(i,j);
                answer[counter] = number;
                counter += 1;
            }
        }
    }

    // compare and sort the connected blocks.
    sort(answer, answer+counter, is_greater_than);
    
    output();
    return 0;
}