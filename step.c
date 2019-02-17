#include <stdio.h>
#include <wiringPi.h>
#include <stdbool.h>
#include <stdlib.h>
#include <sys/stat.h>


#define DELAY 5
#define ROTATION_FACTOR 30 
void setPins(int a,int b,int c,int d);
int sample();
void rotate(int,int);
void writeFile();
void writePosition(int);
int getPosition();

 int pos;
int main (int argc,char** argv)
{
 
  pos=getPosition();
  wiringPiSetup();
  pinMode (0, OUTPUT);
  pinMode(1,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,INPUT);
  writeFile();
  int destination=atoi(argv[1]);
  printf("destination====%d\n",destination);
  printf("pos=====%d\n",pos);
  rotate(pos,destination);
  writePosition(destination);
  setPins(0,0,0,0);
  return 0 ;
}
int getPosition(){
   struct stat stats;
   int exist = stat("/home/pi/Desktop/IOT-Automatic-Pill-Dispenser/position.dat",&stats);
   FILE *ptr=NULL;
   ptr=fopen("/home/pi/Desktop/IOT-Automatic-Pill-Dispenser/position.dat", "r+");

   if(exist==0){

       int num=0;
       fscanf(ptr,"%d",&num);
       fclose(ptr);
       return num;
   }
   else{

        fprintf(ptr,"1");
        printf("hiii\n");
        fclose(ptr);
        return 1; 
   }
   
}
void writePosition(int current){
    
    FILE *fp;
    fp=fopen("/home/pi/Desktop/IOT-Automatic-Pill-Dispenser/position.dat","w");
    fprintf(fp,"%d",current);
    fclose(fp);
    
}
void rotate(int position, int destination){
 int i=0;
 bool direction=destination>position;
 if(direction){
    int spaces=destination-position;
      for (;i<ROTATION_FACTOR*spaces;i++)
      {
        setPins(0,0,1,1);
        delay(DELAY);
        setPins(0,1,0,0);
        delay(DELAY);
        setPins(1,0,0,1);
        delay(DELAY);
        setPins(0,0,1,1);
        delay(DELAY);
      }
  }
  else{
  int spaces=position-destination;
    for (;i<ROTATION_FACTOR*spaces;i++)
      {
        setPins(0,0,1,1);
        delay(DELAY);
        setPins(1,0,0,1);
        delay(DELAY);
        setPins(0,1,0,0);
        delay(DELAY);
        setPins(0,0,1,1);
        delay(DELAY);
      }
  }
}
void setPins(int a,int b, int c, int d){
  digitalWrite(0,a);
  digitalWrite(1,b);
  digitalWrite(2,c);
  digitalWrite(3,d);
}
int sample(){
 int numHigh=0;
 int i=0;
 for(;i<50;i++){
  if(digitalRead(4)==1)
	numHigh++;
  delay(10);
 }
 return (int)(numHigh>=25);
}
void writeFile(){
   FILE *fp;

   fp = fopen("/home/pi/Desktop/IOT-Automatic-Pill-Dispenser/meds.dat", "w");
   fprintf(fp, "%d,%d\n",sample(),pos);	
   fclose(fp);
}
