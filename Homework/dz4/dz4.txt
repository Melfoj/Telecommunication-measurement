z=textread('meas.txt');
x=z (1:2:end);
y=z(2:2:end);
x1=x;
r=8;
x1(length(x1)+1)=max(x)+(max(x) - min(x))/r;
x1(length(x1)+1)=min(x)-(max(x) - min(x))/r;
p=polyfit (x, y, 1);
f=polyval (p,x1);
plot(x, y, 'o', x1, f)
title('Uros i Maja')
xlabel('x')
ylabel('y')
xlim([min(x)-2*(max(x) - min(x))/r, max(x)+2*(max(x) - min(x))/r])
ylim([min(y)-2*(max(x) - min(x))/r, max(y)+2*(max(x) - min(x))/r])
legend('Ucitano','Procena')
