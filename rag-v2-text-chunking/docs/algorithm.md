# Algorithm

## Text Chunking Algorithm

### Step 1

Read PDF.

### Step 2

Extract complete text.

### Step 3

Choose chunk size.

Example:

```
chunk_size = 200
```

### Step 4

Loop through text.

```
for i in range(0, len(text), chunk_size):
```

### Step 5

Slice text.

```
text[i:i+chunk_size]
```

### Step 6

Append chunk to list.

### Step 7

Return list of chunks.

---

## Time Complexity

Reading PDF

O(n)

Chunking

O(n)

Overall

O(n)

---

## Space Complexity

O(n)

because every chunk is stored in memory.