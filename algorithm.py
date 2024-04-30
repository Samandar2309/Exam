from scipy.optimize import linprog

# Optimallashtirish funksiyasining koeffitsiyentlari
c = [-36, -54, -54]  # Funksiyani minimal qiymatini topish uchun koeffitsiyentlar

# Chegara shartlari
A = [[5, 4, 3], [3, 6, 9]]  # Qatorlar
b = [90, 90]  # O'ng tomon

# O'zgaruvchilar chegaralari
x0_bounds = (0, None)  # x0 o'zgaruvchisi manfiy bo'lishi mumkin emas
x1_bounds = (0, None)  # x1 o'zgaruvchisi manfiy bo'lishi mumkin emas
x2_bounds = (0, None)  # x2 o'zgaruvchisi manfiy bo'lishi mumkin emas

# Simpleks usuli orqali optimallashtirish
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

print('Optimal yechimlar:')
print('x1 =', result.x[0])
print('x2 =', result.x[1])
print('x3 =', result.x[2])
print('Optimal qiymat:', -result.fun)  # Funksiyaning eng yaxshi qiymati

