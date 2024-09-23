"""Book Worm"""
def book_counter(dataset_amount):
    """Count the read books in each dataset"""
    for _ in range(dataset_amount):
        book_cnt = 0
        time_cnt = 0
        readable = float(input())
        book_amount = int(input())
        dataset_list = []
        for _ in range(book_amount):
            book_time = float(input())
            dataset_list.append(book_time)
            dataset_list.sort()
        for book in dataset_list:
            if time_cnt + book <= readable:
                time_cnt += book
                book_cnt += 1
        print(book_cnt)
book_counter(int(input()))
