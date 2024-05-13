#define N 800
#define REAL 0
#define IMAG 1
#define PI 3.14159265
 
#include<stdlib.h>
#include<stdio.h>
#include<fftw3.h>
#include<math.h>

float gauss(float x)
{ 
 
  return(exp(-x*x));
}


float FTgauss(float k)
{ 
 
  return((exp((-k*k)/4))/sqrt(2));
}

int main()
{
 
  int i;
  float xmin=-100.0,xmax=100.0,dx=(xmax-xmin)/(N-1),cons=(dx/sqrt(2*PI));
  
  fftw_complex *in, *out ,*factor;
  fftw_plan my_plan;
  in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*N);
  out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*N);
  float *x=(float*)malloc(N*sizeof(float));
  float *k=(float*)malloc(N*sizeof(float));
  factor=(fftw_complex*) fftw_malloc(sizeof(fftw_complex)*N);
  
  for (i = 0; i < N; i += 1)
 {  
    x[i]=xmin+i*dx;
    in[i][REAL]=gauss(x[i]);
    in[i][IMAG]=0.0;
 }
  
 
  my_plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
  fftw_execute(my_plan);
  

  for (i = 0; i < N; i += 1)
 {  
   if(i<(N/2))
    k[i]=(i/(N*dx))*(2*PI);
    
   else
    k[i]=((i-N)/(N*dx))*(2*PI);
   
    factor[i][REAL]=cos(k[i]*x[0]);
    factor[i][IMAG]=sin(-k[i]*x[0]);
 }
 char fname[50];
 sprintf(fname,"fftgauss.txt");
 FILE *fp=fopen(fname,"w");
  for (i = 0; i < N; i += 1)
 {  
   out[i][REAL]=cons*(factor[i][REAL]*out[i][REAL]-factor[i][IMAG]*out[i][IMAG]);
   out[i][IMAG]=cons*(factor[i][REAL]*out[i][IMAG]+factor[i][IMAG]*out[i][REAL]);
   
   
   fprintf(fp,"%f  %f \n",k[i],out[i][REAL]);
 }
  
  fclose(fp);
  fftw_destroy_plan(my_plan);
  fftw_free(in);
  fftw_free(out);
  fftw_free(factor);
  free(k);
  free(x);
}