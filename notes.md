# Coding Patterns Reference

## Hashmaps

 Store elements in a dict to get to **O(1)** time complexity. Replaces O(N^2) brute force nested loops.

* **Initialize** an empty dict.
* **Iterate** through the collection using a loop.
* **Check** if the condition matches the current value or a key currently in the dict.
* **Return** the if condition is met.
* **Store** the current element's data if no match.

keys and values depend on what the problem asks (storing the element value or its index as the key/value)

---

```python
def hashmap_pattern(nums, target):
    lookup = {} # Key: value/complement, Value: index or count

    for index, num in enumerate(nums):
        complement = target - num  # Example condition (e.g., Two Sum)

        if complement in lookup:
            return [lookup[complement], index] # Condition met

     lookup = {} # Key: num, Value: index or count

    return []
```

## Pointers

Use pointer variables to track positions in a collection without needing nested loops or extra copies. Most common for arrays, strings, linked lists, and sorted inputs.

* **Initialize** one or more pointers, usually at the start/end of the collection.
* **Loop** while the pointers are still valid.
* **Check** the current values at each pointer.
* **Return** if the condition is met.
* **Move** one or both pointers based on what the problem asks.

Pointer movement depends on the pattern:

* **Two pointers inward**: start at both ends and move toward the middle.
* **Fast and slow pointers**: move one pointer faster to detect cycles, find middles, or compare positions.
* **Sliding window**: expand one pointer and shrink another to maintain a valid window.

---

```python
def two_pointer_pattern(values, target):
    left = 0
    right = len(values) - 1

    while left < right:
        current = values[left] + values[right]

        if current == target:
            return [left, right]

        if current < target:
            left += 1
        else:
            right -= 1

    return []
```
