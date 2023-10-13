# Nomoto
Nomoto model analytics and prediction

## Модель

Предполагаем, что акселерометр и гироскоп позволяют измерять линейную и угловую скорость судна в локальной системе координат. 
![image](https://github.com/Pernach/Nomoto/assets/19903029/1142e62f-716c-4b4d-8f43-d868f13a345c)

Динамическая модель:
![image](https://github.com/Pernach/Nomoto/assets/19903029/6b517e1e-596d-4a13-813e-e8948c7a63e9)

где
m – масса судна
I_z – присоединенный момент инерции
x_G – продольная координата центра тяжести
Y – компонент поперечных гидродинамических сил
N – компонент продольных гидродинамических сил
u_0 – продольная скорость судна (будем считать постоянной)
v – линейная скорость
r – угловая скорость
δ_R – угол поворота руля
В матричном виде:
![image](https://github.com/Pernach/Nomoto/assets/19903029/b7aabb6a-c659-4816-9a9a-e9c9cfd05b5c)

Модель ВСВ
![image](https://github.com/Pernach/Nomoto/assets/19903029/42a9903c-cfe6-4a75-9100-4101aaeaed28)

[24-31.pdf](https://github.com/Pernach/Nomoto/files/12897015/24-31.pdf)

## Параметры модели

A = [[-3, 2], [0.58, -5]]
B = [[1], [18]]
C = [[1, 0], [0, 1]]
D = [[0], [0]]
min_x0 = [[-1], [-1]]
max_x0 = [[1], [1]]
noise [[0, 0.05], [0, 0.1]]

modeling time 50
sampling time 0.01
input magnitude [[-0.5, 0.5]]

Output fault:
min start 10
max start 40
min duration 5
max duration 40

Multiplicative:
min 0.5
max 5

Constant:
min -10
max 10
