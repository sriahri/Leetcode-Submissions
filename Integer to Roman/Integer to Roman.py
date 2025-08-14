class Solution:
    def intToRoman(self, num: int) -> str:
        s=''
        l1=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        sym=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        i=12
        while num!=0:
            div=num//l1[i]
            num=num%l1[i]
            while div:
                s+=sym[i]
                div-=1
            i-=1
        return s