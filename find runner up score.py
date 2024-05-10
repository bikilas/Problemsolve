if __name__ == '__main__':
    n = int(input())  # Read the number of scores
    arr = list(map(int, input().split()))  # Read the array of scores

    # Sort the list in descending order
    arr.sort(reverse=True)

    # Find the runner-up score
    runner_up = None
    for score in arr:
        if score < arr[0]:
            runner_up = score
            break

    # Print the runner-up score
    print(runner_up)
