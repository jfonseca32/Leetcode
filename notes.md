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

## Windows

Use window boundaries to track a contiguous section of an array or string. Most window problems avoid rebuilding slices by updating counts, sums, or state as the window moves, keeping things O(N).

* **Initialize** left/right boundaries and any state needed for the current window.
* **Expand** or **Shrink** the window by moving the right or left or both boundaries.
* **Update** the state with the new value.
* **Check** if the current window answers the problem or violates a rule.

Depends on how the problem controls size:

* **Dynamic window**: grow and shrink until a condition is valid, usually for "longest" or "minimum length" problems.
* **Fixed window**: keep the window at exactly size `k`, usually for max/min sum, averages, or counts.

---

```python
def dynamic_window_pattern(values):
    left = 0
    state = {}  # Could also be a sum, count, or set
    best = 0

    for right, value in enumerate(values):
        state[value] = state.get(value, 0) + 1

        while not window_is_valid(state):
            left_value = values[left]
            state[left_value] -= 1

            if state[left_value] == 0:
                del state[left_value]

            left += 1

        best = max(best, right - left + 1)

    return best


def fixed_window_pattern(nums, k):
    current = 0
    best = 0

    for right, num in enumerate(nums):
        current += num

        if right >= k:
            current -= nums[right - k]  # Remove value outside window

        if right >= k - 1:
            best = max(best, current)

    return best
```
