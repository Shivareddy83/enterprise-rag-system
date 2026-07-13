# Algorithm

## Lexical Retrieval Algorithm

### Step 1

Read the PDF document.

### Step 2

Extract all document text.

### Step 3

Split the text into fixed-size chunks.

### Step 4

Accept a user query.

### Step 5

Normalize the query by converting it to lowercase.

### Step 6

Split the query into individual keywords.

### Step 7

For each document chunk:

* Convert the chunk to lowercase.
* Count the occurrences of each keyword.
* Calculate the relevance score.

### Step 8

Store all matching chunks with their scores.

### Step 9

Sort results in descending order of relevance score.

### Step 10

Display ranked search results.

---

## Time Complexity

| Operation     | Complexity |
| ------------- | ---------- |
| Read PDF      | O(n)       |
| Chunk Text    | O(n)       |
| Search Chunks | O(n × k)   |
| Ranking       | O(m log m) |

Where:

* **n** = Number of chunks
* **k** = Number of query keywords
* **m** = Number of matching chunks

---

## Space Complexity

O(n)

because all document chunks and matching results are stored in memory.
