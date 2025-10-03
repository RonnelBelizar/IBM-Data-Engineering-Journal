# Topic: Module 2 - Python Data Structures

# 🐍 Python Data Structures (Data Engineering Context)

---

## 📦 Tuples

    • Immutable, ordered collection.  
    • Cannot be changed after creation.  
    • Use Case → Read-only data (e.g., ETL job metadata, configs).  

    Example:
        my_tuple = (1, 2, 3)

    Essential Functions:
        len(my_tuple)        → length of tuple
        my_tuple[i]          → access element by index
        (a, b) = (1, 2)      → unpacking values

---

## 📋 Lists

    • Mutable, ordered collection.  
    • Can be updated, appended, or removed.  
    • Use Case → Dynamic data (e.g., logs, incoming records).  

    Example:
        my_list = [1, 2, 3]
        my_list.append(4)        # add item
        my_list.remove(2)        # remove item
        my_list.sort()           # sort list
        my_list.reverse()        # reverse list

    Essential Functions:
        len(my_list)             → get number of elements
        my_list[i]               → access element by index
        my_list.pop()            → remove last item
        sum(my_list)             → total values
        max(my_list), min(my_list) → find extremes

---

## 📖 Dictionaries

    • Mutable, unordered key-value pairs.  
    • Keys must be unique.  
    • Use Case → Mapping data (e.g., JSON, API responses, schema maps).  

    Example:
        my_dict = {"name": "Alice", "age": 30}
        print(my_dict["name"])           # access value
        my_dict["job"] = "Engineer"      # add new key-value
        my_dict.update({"age": 31})      # update value
        my_dict.pop("job")               # remove key-value

    Essential Functions:
        my_dict.keys()                   → all keys
        my_dict.values()                 → all values
        my_dict.items()                  → all key-value pairs
        "name" in my_dict                → check if key exists
        len(my_dict)                     → count pairs

---

## 🧩 Sets

    • Mutable, unordered collection of unique elements.  
    • Removes duplicates automatically.  
    • Use Case → Deduplication, intersections, unions.  

    Example:
        my_set = {1, 2, 3, 3}
        print(my_set)               # {1, 2, 3}
        my_set.add(4)               # add element
        my_set.remove(2)            # remove element
        my_set.discard(5)           # safe remove (no error)
        my_set.clear()              # empty the set

    Essential Functions:
        set1 | set2                 → union
        set1 & set2                 → intersection
        set1 - set2                 → difference
        set1 ^ set2                 → symmetric difference
        len(my_set)                 → count unique elements

---

## ✨ Quick Recap

    • Tuple  (🔒) → Immutable, Ordered, Allows Duplicates  
        - Access, Unpack, Length  
    • List   (📝) → Mutable, Ordered, Allows Duplicates  
        - Append, Remove, Sort, Pop  
    • Dict   (🔑) → Mutable, Key-Value, Keys Unique  
        - Keys, Values, Items, Update  
    • Set    (🚫) → Mutable, Unordered, No Duplicates  
        - Union, Intersection, Difference  

