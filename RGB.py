import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("C:\\Users\\evans\\OneDrive\\Desktop\\Python\\RGB Channels\\cat.jpg")
assert image is not None, "file could not be read, check with os.path.exists()"

# Define colors and channel indices
colors = ('b', 'g', 'r')  # blue, green, red
channels = (0, 1, 2)  # BGR channel indices

# Create a new figure
plt.figure(figsize=(10, 6))

# Loop through each channel
for i, color in zip(channels, colors):  
    # Extract the channel and plot the histogram
    channel_data = image[:, :, i].ravel()  # Flatten the channel
    plt.hist(channel_data, bins=256, range=[0, 256], color=color, alpha=0.7, label=f'{color.upper()} Channel')

# Add titles and labels
plt.title('Color Channel Histograms')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim([0, 255])
plt.legend()  # Add a legend to identify colors
plt.show()