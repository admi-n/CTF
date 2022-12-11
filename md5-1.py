#coding: utf-8
import hashlib
dic = '0123456789'
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                for e in dic:
                    for f in dic:
                        for g in dic:
                            t = 'ISCTF{md5_is_11'+str(a)+str(b)+'1'+str(c)+str(d)+'8'+str(e)+str(f)+str(g)+'}'  #碰撞
                            md5 = hashlib.md5(t.encode("utf-8")).hexdigest()
                            #print (t)
                            if md5[:32] == '88875458bdd87af5dd2e3c750e534741': #32位数MD5
                                print (t)