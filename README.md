# -Cylinder-sequence-using-Pneumatic
This project automates pneumatic cylinder sequences (A and B) using Python. Users input actions like extension (+) and retraction (-), and the program processes them step-by-step to generate a bar chart, visually displaying each cylinder's state transitions.
Here's a **step-by-step procedure** to execute the Python script and generate the image based on the pneumatic cylinder sequence:
Here’s a detailed **README.md** for your pneumatic cylinder sequence automation project:

---

# Pneumatic Cylinder Sequence Automation

This project automates the sequence of actions for a pneumatic system involving two cylinders (A and B) using Python. Users can define a sequence of cylinder operations (such as extension `+` and retraction `-`) for each cylinder. The program dynamically visualizes the sequence with a functional bar chart showing the states of the cylinders at each step.

## Features
- **Dynamic Sequence Input**: Accepts cylinder actions like `A+`, `B-`, `A-`, etc.
- **Real-Time Visualization**: Displays the state of the cylinders (extended/retracted) for each step in a sequence.
- **Customizable**: You can change the sequence as needed and view updated images.
- **Easy-to-Understand Output**: A simple, functional image that highlights the state transitions (extended/retracted) of each cylinder.

## Requirements
To run this project, you will need:
- **Python 3.x** (tested on version 3.11)
- **Pillow** (for image handling)
- **Matplotlib** (for plotting and visualization)
  
Install the dependencies using pip:
```bash
pip install matplotlib pillow
```

## Project Setup

1. **Download the required images**:
   - **Extended** and **Retracted** images for both cylinders (A and B).
     - Make sure the images are named `extended.png` and `retracted.png`, and are placed in the same directory as the Python script.

2. **Input the sequence**:
   - When running the script, you will be prompted to enter the sequence in the form of `A+`, `A-`, `B+`, `B-`, etc.

3. **Run the script**:
   - Simply run the Python script and provide the sequence as input. The program will generate a functional image showing the cylinder states at each step.
   - Example sequence: `A+ B- A- B+`.

4. **Output**:
   - A functional image (`functional_cylinder_sequence.png`) will be saved in the current directory, showing the sequence with the respective states of cylinders A and B.

## Example Usage

1. **Input**:
   ```bash
   Enter the cylinder sequence (e.g., A+B+A-B-), separated by spaces.
   Sequence: A+ B- A- B+
   ```
   
2. **Output**:
   - The program will generate a visualization with the following steps:
     - **Step 1**: Cylinder A Extended, Cylinder B Retracted
     - **Step 2**: Cylinder A Extended, Cylinder B Retracted
     - **Step 3**: Cylinder A Retracted, Cylinder B Retracted
     - **Step 4**: Cylinder A Retracted, Cylinder B Extended

3. The functional image (`functional_cylinder_sequence.png`) will show the sequence visually, with each cylinder state labeled as "Extended" or "Retracted" for every step.

## Code Explanation

### 1. **get_sequence_input()**:
   Prompts the user to input a sequence for the cylinder actions (e.g., `A+ B- A- B+`).

### 2. **generate_cylinder_sequence_image()**:
   - Loads images for both "Extended" and "Retracted" states.
   - Iterates over the provided sequence, determining the state of each cylinder after each action.
   - Generates a plot showing the state transitions of both cylinders for each step in the sequence.

### 3. **Matplotlib Visualization**:
   - Uses `matplotlib` to create a plot with images representing each cylinder's state.
   - Labels each cylinder state as either "Extended" or "Retracted" below the corresponding image.

### 4. **Output**:
   - The generated sequence is saved as a functional image and displayed.

## Example Sequence and Output

### Example Input:
```bash
Enter the cylinder sequence (e.g., A+B+A-B-), separated by spaces.
Sequence: A+ B- A- B+
```

### Generated Output Image:
- **Step 1**: Cylinder A Extended, Cylinder B Retracted
- **Step 2**: Cylinder A Extended, Cylinder B Retracted
- **Step 3**: Cylinder A Retracted, Cylinder B Retracted
- **Step 4**: Cylinder A Retracted, Cylinder B Extended

![Example output image](functional_cylinder_sequence.png)

## Troubleshooting

- **Error: Image not showing properly**:
  Ensure the `extended.png` and `retracted.png` images are correctly placed in the project directory.
  
- **Invalid Input**:
  If you enter an invalid action (e.g., `C+`), the program will print an error message and stop.

## Contributing

Feel free to fork this project and contribute by:
- Adding more features
- Improving code efficiency
- Enhancing the user interface


---

This README provides the necessary details about the project setup, usage, and functionality. It should help users understand how to use the program, what dependencies are required, and what the output will look like.

![functional_cylinder_sequence](https://github.com/user-attachments/assets/f11db1bb-df84-45c8-a107-5e413809e568)

