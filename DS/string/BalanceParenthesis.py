open=["[","{","("]
close=["]","}",")"]
def check(str):
    st=[]
    for i in str:
        if i in open:
            st.append(i)
        elif i in close:
            pos=close.index(i)
            if len(st) > 0 and open[pos] == st[len(st)-1]:
                st.pop()
            else:
                return "Unbalance"
    if len(st) == 0:
        return "balanced"
    else:
        return "Unbalanced"

s="[{()}]"
print(check(s)) #Balanced