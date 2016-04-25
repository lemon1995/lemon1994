guess_me=7
start=1

while guess_me>start:
    print('too low')
    start+=1

if guess_me==start:
    print('found it')
    start+=1

if guess_me<start:
    print('oops')

    
