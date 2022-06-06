h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

print(f'{((h1 + h2 + (m1 + m2 + (s1 + s2) // 60) // 60)%24).__str__().zfill(2)}:{((m1 + m2 + (s1 + s2) // 60) % 60).__str__().zfill(2)}:{((s1 + s2) % 60).__str__().zfill(2)}')
