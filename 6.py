def isValid(s):
    d = {'{':'}','[':']','(':')'}
    st = []
    for c in s:
        if c in d:
            st.append(c)
            continue
        if not st or c != d[st.pop()]:
            return False
    return not st
