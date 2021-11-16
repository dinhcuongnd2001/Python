start, end, cso = map(int , input().split())

List_num = [0,1,3,5,7] #la cac so dxung dau tien 0,1,11, 101, 111

key = ['', '0', '1']
arr = []
# sinnh nhi phan doi xung: sinh cac day nhi phan tu 1->9 rồi lay doi xung trong cac truong hop: giua 2 day khong co so nao, có so 0 
# hoac co so 1 (vi ta thay so nhi phan doi xung lon nhat < 2_000_000 là so co 21 chu so nhi phan)
# sao khi sinh 1 day nhi phan them so 1 o đầu và cong key va lay đối xưng
# 
def genbin(n, bs=''):
    if len(bs) == n:
        for i in range(len(key)):
            tmp = list(bs)
            tmp.reverse() 
            tmp = ''.join(tmp) #tao day nguoc
            res =  '1' + bs + key[i] + tmp + '1' #tao day doi xung 
            if len(res) == 21: #voi nhung day co 21 chu so kiem tra xem so khi chuyen sang thap phan co bi quá 2_000_000 khong
                if chuyennhiphan(res) <= 2000000:
                    arr.append(chuyennhiphan(res))
            else:
                arr.append(chuyennhiphan(res))
    else:
        genbin(n, bs + '0')
        genbin(n, bs + '1')

def chuyennhiphan(num):
    dem = 0
    sum = 0
    for i in range(len(num)-1,-1,-1):
        sum += int(num[i])*(2**dem)
        dem+=1
    return sum


for i in range(1,10):
    arr.clear()
    genbin(i)
    List_num.extend(arr)

List_num.sort() #sap xep lai vi khi sinh 1 so số khong them thu tu


def chuyencso(num, cso): #chuyen 1 so cso 10 ve cso bat ki
    res = []
    while num!=0:
        res.append(num%cso)
        num = int(num/cso)
    res.reverse()
    res = ''.join([str(i) for i in res])
    return res

def check(num): #kiem tra tinh doi xung 1 chuoi
    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            return False
    return True




count = 0
for num in List_num:
    if num > end:
        break
    elif num < start:
        continue
    else:
        check_num = True
        for cs in range(2, cso+1):
            if not check(chuyencso(num,cs)):
                check_num = False
                break
        if check_num:
            count += 1
print(count)