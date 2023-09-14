%% 1
figure;
%1
ux = 0:0.01:2*pi;
U = u(ux);
myplot(ux, U, 1, 'red', '-', "U(x)");
hold on;

%2
fx = -0.9:0.01:0.9;
F = f(fx);
myplot(fx, F, 2, 'blue', '--', "F(x)");

%3
gx = 0.5:0.01:1.5;
G = g(gx);
myplot(gx, G, 3, 'black', ':', "G(x)");

%4
hx = 0:0.01:1;
H = h(hx);
myplot(hx, H, 4, 'yellow', '-', "H(x)");
%% 2
[zx, zy] = meshgrid(-1:0.01:1, -1:0.01:1);
Z = z(zx, zy);
myplot3(zx, zy, Z, "Z(x, y)");

[wx, wy] = meshgrid(0:0.01:1, 0:0.01:1);
W = w(wx, wy);
myplot3(wx, wy, W, "W(x, y)");
%% 3
% решил не делать, так как это просто набор действий из предыдущих глав,
% только в функциях
%% 1
function myplot(x, y, pos, color, line, name)
    subplot(2, 2, pos);
    plot(x, y, "Color", color, "LineStyle", line);
    xlabel("x");
    ylabel("y");
    title(name);
    grid on;
end

function u0 = u(x)
    u0 = sin(log10(x + 1)) + cos(log10(x + 1));
end

function f0 = f(x)
    f0 = (1 ./ (1  + 1 ./ (1 + x)));
end

function g0 = g(x)
    g0 = x.^(x.^(x));
end

function h0 = h(x)
    h0 = sin(6 * pi * abs(x - 2/3) .* x.^2);
end
%% 2
function z0 = z(x, y)
    z0 = exp(3 .* x .* sin(0.5 * pi .* y)) + exp(3 .* y .* sin(0.5 * pi .* x));
end

function w0 = w(x, y)
    w0 = sin(exp(2 .* x) - exp(-2 .* y)) + cos(exp(2 .* y) - exp(-2 .* x));
end

function myplot3(x, y, z, name)
    figure;
    mesh(x, y, z);
    xlabel("x");
    ylabel("y");
    zlabel("z");
    title(name);
end
