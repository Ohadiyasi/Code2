scores = [int(item) for item in (input('Type scores: (format: 15, 16, 17) ').split(', '))]
average = sum(scores)/len(scores)
if average >= 17: print('Great!')
elif average >=12: print('Normal!')
else: print('Failed!')