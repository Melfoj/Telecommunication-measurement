clear all
pkg load statistics;
f=fopen('lab4.txt','r'); 
x=fscanf(f,'%f'); 
n=length(x); 
figure,hist(x,n),title("Hist") 
figure,boxplot(x),xlim([0 2]), title("BD") 
MO=mean(x) 
SD=std(x)
a=0.05
c=norminv(1-a/2)
CId=MO-c*SD/sqrt(length(x))
CIg=MO+c*SD/sqrt(length(x)) 
y = -3:.01:3;
r=normcdf(y);
figure, cdfplot(x), hold on, plot(y,r), hold off
