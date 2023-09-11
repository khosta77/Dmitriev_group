x = 0; y = 11;
% 1
Z_sqrt3 = (x - sin(y))^(1/3);
Z_sqrt = sqrt(1 - x^2);
Z = atan(Z_sqrt3/Z_sqrt - (abs(x) * Z_sqrt)/Z_sqrt3)

% 2
T_sin = (sin(y) + sin(2 * y) + sin(3 * y));
T_exp = (1 + exp(x));
T_1se = (1 + T_sin/T_exp);
T = (T_sin^4)/T_1se + sqrt(T_1se)

% 3
W_ln = log10(y);
W_tg = (x + tan(y));
W = (1 + W_ln/W_tg) ^ (1 + W_tg/W_ln)

% 4
R_mln = sqrt(abs(x - log10(y)));
R_pln = (x + log10(y));
R = sinh((R_pln^3)/R_mln) * cosh(R_mln * R_pln)

% 5
H_cs = (cos(2 * y) + sin(4 * y));
H_exp = (exp(x) + exp(-x));
H = sqrt(H_cs + sqrt(H_exp))/(H_exp^3 * (H_cs - 2)^2)

% 6
A_3x = x * (1 + x)^2 * (1 + 2 * x) ^ 3;
A_ln = log10(cot(y));
A = (A_3x + (A_3x/A_ln)^(1/3))^5

% 7
S_p = (x - sin(y)); S_m = (x + sin(y));
S = atan(sqrt(abs((S_p/S_m) + (S_m/S_p)))) + exp(S_m * S_p)

% 8
B_arcsin = (1 + asin(cos(2 * y)));
B_23 = (2 ^ x + 3 ^ (-x));
B = B_arcsin / B_23 + ((B_23 - 1)/B_arcsin)^2