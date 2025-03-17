# Password Cracker

[Watch the demo](https://github.com/cris-mbici/brute_force/raw/main/brute_force_demo.mp4). This project is a **password-cracking tool** that attempts to guess a target password using two methods:
- **Dictionary Attack:** Quickly checks for common passwords from a `.csv` file.
- **Brute Force Attack:** Systematically generates and tests all possible character combinations until the correct password is found.

## Key Features
✅ Efficient character set filtering for faster brute force attempts  
✅ Real-time guess tracking (optional)  
✅ Adaptive progress updates for better user experience  
✅ Built-in timer to measure the duration of each attempt

## Note:
❌ The program tends to break down when trying long passwords while viewing attempt.

---

## What I Learned
### 1. **Input Validation**
- Ensuring user input is valid is crucial. For example, I initially wrote this condition incorrectly:
```python
if view_attempts == 'y' or 'n':  # Not Corresto
```
This was always `True`. I corrected it to:
```python
if view_attempts in ['y', 'n']:  # Correct
```
This improved reliability and prevented unexpected behavior.

### 2. **Efficient Character Set Filtering**
- I learned that reducing the number of characters to test drastically improves performance. By identifying which types of characters are present (e.g., lowercase, digits), I reduced unnecessary combinations.

### 3. **Working with External Data**
- I integrated a `.csv` file of common passwords to attempt faster guesses before starting the slower brute force process. This cemented my understanding of external file handling.

### 4. **User Experience Enhancement**
- I added progress updates in the brute force phase to keep users informed about the guessing process. Implementing an adaptive update frequency improved clarity without overwhelming the user with constant messages.

### 5. **Error Handling & Edge Cases**
- I learned the importance of handling special cases, such as:
  - Empty passwords
  - Extremely long passwords (which may cause performance issues)

### 6. **Time Complexity Awareness**
- Writing this project gave me a deeper understanding of how brute force and dictionary attacks differ in performance. I learned that minimizing the character set and implementing smarter guessing strategies can significantly reduce guess attempts.

---

## How to Run the Code
1. Ensure Python is installed on your system.
2. Place a file called `common_pass.csv` in the same folder as the script. This file should contain common passwords (one per line).
3. Run the script and follow the prompts to:
   - Enter a target password.
   - Choose whether to display guesses or only the final result.
4. Observe the results, including the number of attempts and time taken.

---

## Final Thoughts
This project was a valuable learning experience that strengthened my understanding of Python fundamentals, algorithm design, and user experience considerations. I'm excited to continue refining and expanding it!

