k, a, s = map(int, input('Введите результаты Кирилла, Арины и Сережи через пробел: ').split())
if k > a and k > s:
    print(k)
if a > s and a > k:
    print(a)
if s > a and s > k:
    print(s)
