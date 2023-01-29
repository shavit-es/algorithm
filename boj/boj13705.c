#include <stdio.h>
#include <math.h>

__float128 pi = 3.1415926535897932384626433832795028841971693993751058q;
typedef __float128 f;

f Sin(f x) {
    f x_ = x;
    if(x_<0) x_=-x_;
    long mok = x_/(2*pi);
    x_=x_-mok*(2*pi);
    
    f result= x_;
    f hang = x_;
    for (int i = 1; i<50; i++) {
        hang = (-1)*hang*x_*x_/((2*i+1)*(2*i));
        result += hang;
    }
    
    if(x<0.0q) return -1*result;
    else return result;
}

f lb,rb,mid;
long double a,b,c;
int main(){
    scanf("%Lf %Lf %Lf", &a, &b, &c);
    lb=(c-b)/a; //무조건 근이 범위 안에 있는 lower bound
    rb=(c+b)/a; //무조건 근이 범위 안에 있는 upper bound
    while(rb-lb>0.000000000000000000000000001){ 
        mid=(lb+rb)/2;
        f it=a*mid+b*Sin(mid);
        
        if(it<c){
            lb=mid;
        }else{
            rb=mid;
        }
    }
    mid=(lb+rb)/2; //근 값
    long double result = ((long)(1000000.0*(mid+0.0000005)))/1000000.0; //1000000을 곱한뒤에 정수형으로 바꿔서 다시 나눠주기(반올림) -> long은 버림
    printf("%.6Lf",result);
}