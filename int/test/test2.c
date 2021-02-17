#include<stdio.h>
int f(int x){
    if (x<=1){return 0;}
    else if(x%2==0){return f(x+1)+x;}
    else{return f(x-3)-x;}
}
int main(){
    int n=1000;
    int counter=0;
    for(int i=0;i<n;i++){
      for(int j=i;j<n;j++){
        for(int h=j;h<n;h++){
          counter++;
      
        }
      
      }
    }
    printf("%d",counter);
    return 0;
}