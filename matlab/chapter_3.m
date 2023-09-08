%% 1
x = 0.01:0.05:2*pi
f = sin(x)./x
g = exp(-x).*cos(x)

% В отдельных окнах
figure;
f1 = f(find(f > 0)); xf1 = x(find(f > 0));
f2 = f(find(f < 0)); xf2 = x(find(f < 0));
plot(xf1, f1, 'bo-', xf2, f2, 'rx-');
title('График 1');
legend('f(x) > 0', 'f(x) < 0', 'Location',"best");
xlabel('мм');
ylabel('м');
grid on;
figure;
g1 = g(find(g > 0)); xg1 = x(find(g > 0));
g2 = g(find(g < 0)); xg2 = x(find(g < 0));
plot(xg1, g1, 'ms-.', xg2, g2, 'k*-');
title('График 2');
legend('g(x) > 0', 'g(x) < 0', 'Location',"best");
xlabel('м^3');
ylabel('м_1');
grid on;

% 
figure;
plot(xf1, f1, 'bo-', xf2, f2, 'rx-', xg1, g1, 'ms-.', xg2, g2, 'k*-');
title('График 3');
legend('f(x) > 0', 'f(x) < 0', 'g(x) > 0', 'g(x) < 0', 'Location',"best");
xlabel('м^3');
ylabel('м_1');
grid on;

%
figure;
subplot(2, 1, 1);
plot(xf1, f1, 'bo-', xf2, f2, 'rx-');
title('График 1');
legend('f(x) > 0', 'f(x) < 0', 'Location',"best");
xlabel('мм');
ylabel('м');
grid on;
subplot(2, 1, 2);
plot(xg1, g1, 'ms-.', xg2, g2, 'k*-');
title('График 2');
legend('g(x) > 0', 'g(x) < 0', 'Location',"best");
xlabel('м^3');
ylabel('м_1');
grid on;

%% 2

%% 3