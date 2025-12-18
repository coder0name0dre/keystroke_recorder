# Keystroke Recorder

This script is a simple, ethical keystroke recorder written in Python.

It records only the text that a user intentionally types into the program itself, ads a timestamp to each entry, and saves the result to a local text file.

---

## Requirements

- Python 3.x
- No third party libraries required (standard library only)

---

## How To Run

1. Clone or download this the repository:

```
git clone https://github.com/coder0name0dre/keystroke_recorder.git
cd keystroke_recorder
```

2. Open a terminal in the project folder
3. Run the script:

**Windows**

```
python keystroke_recorder.py
```

**macOS / Linux**

```
python3 keystroke_recorder.py
```

---

## Usage

1. The program will display instructions in the terminal
2. Type any text and press **Enter**
3. Each entry is saved with a timestamp
4. Type `QUIT` and press **Enter** to stop the program

---

## Output

The program creates (or appends to) a file named:

```
keystrokes_recording.txt
```

### Example Output:

```
2025-12-16 14:45:01 - Hello
2025-12-16 14:45:10 - Learning Python
```

---

