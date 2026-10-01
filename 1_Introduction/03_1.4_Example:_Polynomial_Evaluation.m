% 03_1.4_Example:_Polynomial_Evaluation

%

%Lecture: /1_Introduction
%Content: 03_1.4_Example:_Polynomial_Evaluation

%
function result = horner_method(coefficients, x)
    % 使用Horner方法计算多项式在x处的值
    % coefficients: 多项式系数向量，从最高次到常数项
    % x: 计算点
    % result: 多项式在x处的值
    
    n = length(coefficients);
    result = coefficients(1);
    for i = 2:n
        result = result * x + coefficients(i);
    end
end


function result = evaluate_polynomial(coefficients, x)
    % 使用直接求值法计算多项式在x处的值
    % coefficients: 多项式系数向量，从最高次到常数项
    % x: 计算点
    % result: 多项式在x处的值
    
    n = length(coefficients);
    result = 0;
    for i = 1:n
        result = result + coefficients(i) * x^(n-i);
    end
end

% 比较两种方法的结果
coefficients = [2, -6, 2, -1];  % 2x^3 - 6x^2 + 2x - 1
x = 3;
horner_result = horner_method(coefficients, x);
direct_result = evaluate_polynomial(coefficients, x);

fprintf('Horner方法结果: %.6f\n', horner_result);
fprintf('直接求值法结果: %.6f\n', direct_result);
fprintf('误差: %.6f\n', abs(horner_result - direct_result));



function condition_number = polynomial_condition_number(coefficients, x)
    % 计算多项式在x处的条件数
    % coefficients: 多项式系数向量，从最高次到常数项
    % x: 计算点
    % condition_number: 多项式在x处的条件数
    
    polynomial_value = horner_method(coefficients, x);
    sum_of_terms = 0;
    n = length(coefficients);
    for i = 1:n
        sum_of_terms = sum_of_terms + abs(coefficients(i) * x^(n-i));
    end
    condition_number = sum_of_terms / abs(polynomial_value);
end

condition_number = polynomial_condition_number(coefficients, x);
fprintf('多项式在x=%.2f处的条件数: %.6f\n', x, condition_number);



function root = polynomial_root_bisection(coefficients, low, high, tol)
    % 使用二分法求解多项式的零点
    % coefficients: 多项式系数向量，从最高次到常数项
    % low: 区间下限
    % high: 区间上限
    % tol: 收敛阈值 (默认值: 1e-7)
    % root: 零点
    
    if nargin < 4
        tol = 1e-7;
    end
    
    while (high - low) / 2 > tol
        mid = (low + high) / 2;
        f_low = horner_method(coefficients, low);
        f_mid = horner_method(coefficients, mid);
        if f_mid == 0
            root = mid;
            return;
        elseif f_low * f_mid < 0
            high = mid;
        else
            low = mid;
        end
    end
    
    root = (low + high) / 2;
end

root = polynomial_root_bisection(coefficients, 0, 3);
fprintf('多项式的零点: %.6f\n', root);