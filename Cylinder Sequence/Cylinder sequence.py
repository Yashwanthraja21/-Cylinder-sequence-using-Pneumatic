import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_sequence_input():
    """
    Prompt the user to enter a pneumatic cylinder sequence.
    """
    print("Enter the cylinder sequence (e.g., A+B+A-B-), separated by spaces.")
    sequence = input("Sequence: ").split()
    return sequence

def generate_cylinder_sequence_image(sequence):
    """
    Generate a functional image showing the sequence of pneumatic cylinder operations.
    """
    # Load images for "Extended" and "Retracted" states
    extended_img = Image.open("extended.png")
    retracted_img = Image.open("retracted.png")

    # Initialize cylinder states
    a_state = "Retracted"
    b_state = "Retracted"
    states = []

    # Process each step in the sequence
    for step in sequence:
        if step == "A+":
            a_state = "Extended"
        elif step == "A-":
            a_state = "Retracted"
        elif step == "B+":
            b_state = "Extended"
        elif step == "B-":
            b_state = "Retracted"
        else:
            print(f"Invalid step: {step}. Please use A+, A-, B+, or B-.")
            return None
        
        # Append the state after this step
        states.append((a_state, b_state))

    # Visualization settings
    num_steps = len(sequence)
    y_positions = np.arange(num_steps)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (step, (a_state, b_state)) in enumerate(zip(sequence, states)):
        # Add image for Cylinder A
        if a_state == "Extended":
            ax.imshow(extended_img, extent=[0.1, 0.5, y_positions[i] - 0.3, y_positions[i] + 0.3], aspect='auto')
            ax.text(0.3, y_positions[i] - 0.4, "Extended", va="top", ha="center", fontsize=10)
        else:  # Retracted
            ax.imshow(retracted_img, extent=[0.1, 0.5, y_positions[i] - 0.3, y_positions[i] + 0.3], aspect='auto')
            ax.text(0.3, y_positions[i] - 0.4, "Retracted", va="top", ha="center", fontsize=10)

        # Add image for Cylinder B
        if b_state == "Extended":
            ax.imshow(extended_img, extent=[0.6, 1.0, y_positions[i] - 0.3, y_positions[i] + 0.3], aspect='auto')
            ax.text(0.8, y_positions[i] - 0.4, "Extended", va="top", ha="center", fontsize=10)
        else:  # Retracted
            ax.imshow(retracted_img, extent=[0.6, 1.0, y_positions[i] - 0.3, y_positions[i] + 0.3], aspect='auto')
            ax.text(0.8, y_positions[i] - 0.4, "Retracted", va="top", ha="center", fontsize=10)

        # Step label
        ax.text(1.5, y_positions[i], f"Step {i + 1}: {step}", va="center", ha="left", fontsize=12)

    # Customize the plot
    ax.set_yticks(y_positions)
    ax.set_yticklabels([f"Step {i + 1}" for i in range(num_steps)])
    ax.set_xlim(0, 2.5)
    ax.set_ylim(-0.5, num_steps - 0.5)  # Ensure all steps are visible
    ax.set_xlabel("Cylinder States")
    ax.set_title("Pneumatic Cylinder Sequence")
    ax.axis("off")

    # Save the functional image
    plt.savefig("functional_cylinder_sequence.png")
    print("Functional image saved as 'functional_cylinder_sequence.png'.")

    # Show the plot
    plt.show()

# Main execution
if __name__ == "__main__":
    sequence = get_sequence_input()  # Get user input for the sequence
    if sequence:
        generate_cylinder_sequence_image(sequence)  # Generate the functional image
