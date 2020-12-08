def get_z_array(s,z):
    n=len(s)
    l=0
    r=0
    k=0
    for i in range(1,n):
        if(i>r):
            l,r=i,i
            while r<n and s[r]==s[r-l]:
                r+=1
            z[i]=r-l    #difference between maps to string before $ indexes
            r=r-1   #decrement it because we had to increment it in the while condition which didn't match
        else:
            k=i-l   #k is the index of where i stands in the 'alpha' substring
            if(z[k]<r-i+1):      # 'alpha' inclusive(hence plus 1) of 'i' should be less than 'beta'
                z[i]=z[k]
            else:
                l=i
                while r<n and s[r]==s[r-l]:
                    r+=1
                z[i]=r-l
                r-=1
def search(text,pattern):
    s=pattern+'$'+text;
    z=[0]*len(s)
    get_z_array(s,z)
    for i in range(len(s)):
        if(z[i]==len(pattern)):
            print("pattern found at index",i," :",s[i:i+len(pattern)])
if __name__ == "__main__":
    text = "abcdeaaaa|abcde|gcababchgabhgdghsbhafhchaabcdjhefjerhejaabc";
    pattern = "abc"
    search(text,pattern)
