"""Duplicate I"""
def redundancy_finder(m, n):
    """Find those students who are in both group"""
    m_list = []
    n_list = []
    redundant = []
    for _ in range(m):
        m_list.append(input())
    for _ in range(n):
        n_list.append(input())
    for student in m_list:
        if student in n_list:
            redundant.append(student)
    redundant.sort(reverse=True)
    if not redundant:
        print("Nope")
    else:
        for student in redundant:
            print(student)
redundancy_finder(int(input()), int(input()))
