import numpy as np

# 約数を高速に求める関数（改造版）
def make_divisors(n):
	divisors = []
	for i in range(1, int(n**0.5)+1):
		if n % i == 0 and n//i < 65535:
			if i != n // i:
				divisors.append((i, n//i))
				divisors.append((n//i, i))
			else:
				divisors.append((i, n//i))
	return divisors


def calcTimParameter(tim_clock, interrupt_hz):
	# clock / ab = hz
	ab = int(round(tim_clock / interrupt_hz, 0))

	params = make_divisors(ab)
	if params == []:
		# 条件に一致する組が存在しない場合は
		# 誤差の大きい方に切り替えて再計算（逆四捨五入）
		f = int(((tim_clock / interrupt_hz) * 10)) % 10
		if f < 5:
			ab += 1
		else:
			ab -= 1
		params = make_divisors(ab)
	
	params = sorted(params)
	real_freq = tim_clock/ab
	return (real_freq, params)


def main():
	print('Calculate TIM Values For STM32F4')
	key = input('Interrupt Frequency (HZ):')
	pur = int(key)

	print("TIM1, 8, 9, 10, 11 -> 84000000(Hz)")
	print("Other              -> 42000000(Hz)")
	key = input('Clock Base Line (Hz): ')
	base_c = int(key)
	base_c = base_c * 2
	print("***************************************")
	print("Goal:{}(Hz) TIM_DefaultFreq:{}".format(pur, base_c))
	print("***************************************")

	real_freq, values = calcTimParameter(base_c, pur)

	print("real freq: ", real_freq, " Hz")

	print("TIM_Prescaler | TIM_Period")
	print("--------------------------")
	for psc, arr in values:
		print('%13d | %10d' % (psc-1, arr-1))
	input('Please, Enter key...')


if __name__ == "__main__":
	main()
	











