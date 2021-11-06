import random; from os.path import dirname, abspath, os
count = 0
dest = dirname(abspath(__file__))
list = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]
print("\n--- Windows 95 key generator --- txt version")
print("Made by MATIEO33\n")
arg = int(input('How much keys do you wish to generate? '))
location = os.path.join(dest, "keys.txt")
f = open(location, "w+")
f.write("--- Windows 95 key generator ---\n")
f.write("IMPORTANT NOTE: from my experience, not all keys work, my dearest apologies.\n")
f.write("\n")
f.close()

def gen():
    global aa,ab,ac,ad,ae,af
    aa = random.randint(1, 9)
    ab = random.randint(1, 9)
    ac = random.randint(1, 9)
    ad = random.randint(1, 9)
    ae = random.randint(1, 9)
    af = random.randint(1, 9)


def process():
    global af
    resolved = 0
    gen()
    while resolved == 0:
        while af == 0 or 8 or 9:
            af = random.randint(1, 9)
            if af != 0 or 8 or 9:
                resolved = 1
                process2()
                break

def process2():
    global whole
    whole = aa+ab+ac+ad+ae+af
    if whole % 7 == 0:
        restprocess()
    elif whole % 7 != 0:
        process()

def restprocess():
    global count
    count += 1
    a = random.randint(int("1"), int("366"))
    b = random.choice(list)
    c = str("-OEM-")
    d = 0
    e = int(str(aa) + str(ab) + str(ac) + str(ad) + str(ae) + str(af))
    f = random.randint(10000, 99999)
    line = str("-")
    z = ""
    if a < 100 and a >= 10:
        z = "0"
    elif a < 100 and a < 10:
        z = "00"
    if z == "0" or "00":
        key = str(z) + str(a) + str(b) + str(c) + \
            str(d) + str(e) + line + str(f)
    else:
        key = str(a) + str(b) + str(c) + str(d) + str(e) + line + str(f)
    print("Key: " + str(count) + " sucessfully written!")
    with open(location, 'a') as f:
        f.writelines(key + "\n")
        f.close()
    if count == int(arg):
        print("\n Sucess! All keys have been writted sucessfully. \n")
        os.startfile(dest)

for i in range(int(arg)):
    process()