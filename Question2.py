
# This script processes two cat images as per the exam instructions:
# 1. Extracts a Region of Interest (ROI) from both images
# 2. Applies Canny edge detection to both ROIs
# 3. Performs a bitwise AND operation on the edge maps
# 4. Displays and saves all results in 'output_file_qno2' folder

import cv2
import matplotlib.pyplot as plt
import os

def main():
    # Define input and output folders
    input_folder = 'Input_file'
    output_folder = 'output_file_qno2'
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    # Load both cat images from the input folder
    img1 = cv2.imread(os.path.join(input_folder, 'cat1.jpg'))
    img2 = cv2.imread(os.path.join(input_folder, 'cat2.jpg'))

    # Check if images are loaded correctly
    if img1 is None or img2 is None:
        print("Error: Could not load cat1.jpg or cat2.jpg from Input_file.")
        return

    # Resize both images to the same dimensions for consistency
    img1 = cv2.resize(img1, (500, 400))
    img2 = cv2.resize(img2, (500, 400))

    # -----------------------------
    # Task 1: ROI Extraction
    # -----------------------------
    # Manually specify the ROI (cat's face) coordinates
    # Adjust these numbers if your images are different
    y1, y2 = 100, 300
    x1, x2 = 150, 400

    roi_cat1 = img1[y1:y2, x1:x2]
    roi_cat2 = img2[y1:y2, x1:x2]

    # Save ROIs
    cv2.imwrite(os.path.join(output_folder, 'roi_cat1.jpg'), roi_cat1)
    cv2.imwrite(os.path.join(output_folder, 'roi_cat2.jpg'), roi_cat2)

    # Display the original image and the cropped face (ROI) side by side for cat1
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title("Original Image - Cat1")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(roi_cat1, cv2.COLOR_BGR2RGB))
    plt.title("ROI - Cat1 Face")
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'cat1_and_roi1.png'))
    plt.show()

    # -----------------------------
    # Task 2: Canny Edge Detection
    # -----------------------------
    # Convert the ROIs to grayscale as Canny requires a single-channel input
    roi_cat1_gray = cv2.cvtColor(roi_cat1, cv2.COLOR_BGR2GRAY)
    roi_cat2_gray = cv2.cvtColor(roi_cat2, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection to both grayscale ROIs
    edges_cat1 = cv2.Canny(roi_cat1_gray, 100, 200)
    edges_cat2 = cv2.Canny(roi_cat2_gray, 100, 200)

    # Save edge-detected images
    cv2.imwrite(os.path.join(output_folder, 'edges_cat1.jpg'), edges_cat1)
    cv2.imwrite(os.path.join(output_folder, 'edges_cat2.jpg'), edges_cat2)

    # Display the edge-detected results for both ROIs
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(edges_cat1, cmap='gray')
    plt.title("Canny Edges - ROI 1")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(edges_cat2, cmap='gray')
    plt.title("Canny Edges - ROI 2")
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'canny_edges.png'))
    plt.show()

    # -----------------------------
    # Task 3: Bitwise AND Operation
    # -----------------------------
    # Ensure both edge images are the same size before combining them
    if edges_cat1.shape != edges_cat2.shape:
        edges_cat2 = cv2.resize(edges_cat2, (edges_cat1.shape[1], edges_cat1.shape[0]))

    # Perform a bitwise AND operation to highlight the overlapping edges
    bitwise_and = cv2.bitwise_and(edges_cat1, edges_cat2)

    # Save the AND result
    cv2.imwrite(os.path.join(output_folder, 'bitwise_and.jpg'), bitwise_and)

    # Display the final comparison — showing both edge maps alongside the AND result
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(edges_cat1, cmap='gray')
    plt.title("Canny Edges - ROI 1")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(edges_cat2, cmap='gray')
    plt.title("Canny Edges - ROI 2")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(bitwise_and, cmap='gray')
    plt.title("Bitwise AND Result")
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'bitwise_and_result.png'))
    plt.show()

    print(f"All output images have been saved in the folder: {output_folder}")

if __name__ == "__main__":
    main()