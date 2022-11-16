import hashlib

key = 'bgvyzdsv'
ans = 0

while True:
    possible_key = key + str(ans)
    hash = hashlib.md5(possible_key.encode()).hexdigest()
    if hash[0:5] == '00000':
        break
    ans += 1
    
print('5 leading 0s:', ans)


key = 'bgvyzdsv'
ans = 0

while True:
    possible_key = key + str(ans)
    hash = hashlib.md5(possible_key.encode()).hexdigest()
    if hash[0:6] == '000000':
        break
    ans += 1

print('6 leading 0s:', ans)

