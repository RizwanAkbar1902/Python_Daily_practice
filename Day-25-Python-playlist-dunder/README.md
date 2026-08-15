\# Playlist Manager (Python Dunder Methods)



Small script I wrote today to understand how Python's built-in magic (dunder) methods work behind the scenes.



Instead of writing custom `.display()` or `.count()` functions, I implemented `\_\_str\_\_` and `\_\_len\_\_` to make custom objects behave like native Python types.



\### What it does:

\- `Song` class stores song metadata and formats duration into `mm:ss` via `\_\_str\_\_`.

\- `Playlist` class groups songs together.

\- Calling `len(playlist)` returns the total song count directly.

\- Calling `print(playlist)` neatly prints the whole tracklist.



\### Running the code:

```bash

python playlist.py

