def hanoi(n, start, end, mid):
    if n == 0:
        return
    hanoi(n - 1, start, mid, end)
    print(f"Move disk {n} from {start} to {end}")
    hanoi(n - 1, mid, end, start)


hanoi(3, "s", "e", "t")
