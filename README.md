# -Cylinder-sequence-using-Pneumatic
This project automates pneumatic cylinder sequences (A and B) using Python. Users input actions like extension (+) and retraction (-), and the program processes them step-by-step to generate a bar chart, visually displaying each cylinder's state transitions.
Here's a **step-by-step procedure** to execute the Python script and generate the image based on the pneumatic cylinder sequence:

---

### **Step 1: Install Python and Required Libraries**
1. **Install Python**:
   - Ensure Python (version 3.7 or later) is installed on your system.
   - Download it from [Python's official website](https://www.python.org/downloads/) if needed.

2. **Install Required Libraries**:
   - Open your terminal (Command Prompt, PowerShell, or any shell).
   - Run the following command to install `matplotlib`:
     ```bash
     pip install matplotlib
     ```

---

### **Step 2: Save the Python Script**
1. Open a text editor (like Notepad, VS Code, or Jupyter Notebook).
2. Copy the Python code provided above into the editor.
3. Save the file with a `.py` extension, e.g., `pneumatic_sequence.py`.

---

### **Step 3: Run the Python Script**
1. Open your terminal and navigate to the directory where you saved the script:
   ```bash
   cd path/to/your/script
   ```
2. Execute the script:
   ```bash
   python pneumatic_sequence.py
   ```

---

### **Step 4: Input the Cylinder Sequence**
1. When prompted, input the sequence of cylinder actions.
   - Example: For the sequence `A+ B+ A- B-`, type:
     ```plaintext
     A+ B+ A- B-
     ```
2. Press **Enter**.

---

### **Step 5: View and Save the Output**
1. The script will:
   - Generate a horizontal bar chart showing the states of cylinders A and B for each step.
   - Save the output image as `functional_cylinder_sequence.png` in the same directory as the script.

2. The terminal will display:
   ```plaintext
   Functional image saved as 'functional_cylinder_sequence.png'.
   ```

3. Open the file `functional_cylinder_sequence.png` to view the visualized cylinder sequence.

---

### **Step 6: Upload the Output**
1. If required, navigate to the directory where the `functional_cylinder_sequence.png` is saved.
2. Upload the file to your desired platform (email, cloud storage, or any specific portal).

---

### **Common Issues and Fixes**:
1. **`matplotlib` Not Installed**:
   - Ensure you install `matplotlib` with:
     ```bash
     pip install matplotlib
     ```
2. **Invalid Input Format**:
   - The input must be actions like `A+`, `A-`, `B+`, or `B-` separated by spaces.
   - Example: `A+ B- A- B+`

3. **No Image Generated**:
   - Verify the directory where the script is saved and executed.
   - Ensure the input sequence is valid.

