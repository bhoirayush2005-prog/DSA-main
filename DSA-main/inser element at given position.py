def  insertAtPosition(arr: List[int], X: int, P: int) -> List[int]:
    if not arr or P < 0 or P >= len(arr):
        return arr
    return arr[:P] + [X] + arr[P:-1]