"""sequnceXI"""
def main(n):
    """process"""
    k_of_sequence = (n * 2) - 1
    for row in range(1, k_of_sequence+1):
        for col in range(1, k_of_sequence+1):
            print(f"{min(row, col, (n*2-row), (n*2-col)):02d}", end=" ")
        print()
main(int(input()))
