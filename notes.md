# Coding Patterns Reference

## Hashmaps

Store elements in a dict to get to **O(1)** time complexity. Replaces \(O(N^2)\) brute force nested loops.

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
            
        lookup[num] = index # Store for future iterations
        
    return []
```
