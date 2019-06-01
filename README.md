# Calcurate timer parameter for STM32

## Description
Calcurate STM32's timer parameters, prescaller and autoreload.

## How to use
Sample following.  
interrupt freq: 311 Hz  
STM32 clock: full speed (168MHz)  
```
$> py .\CalcTIMValue2_py3.py
Calculate TIM Values For STM32F4
Interrupt Frequency (HZ):311
TIM1, 8, 9, 10, 11 -> 84000000(Hz)
Other              -> 42000000(Hz)
Clock Base Line (Hz): 84000000
***************************************
Goal:311(Hz) TIM_DefaultFreq:168000000
***************************************
real freq:  310.9999574226249  Hz
TIM_Prescaler | TIM_Period
--------------------------
           96 |       5568
         5568 |         96
```
