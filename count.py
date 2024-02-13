# Count images in each state folder
import os


def count_images_in_state_folder(state_folder):
    try:
        image_count = len([f for f in os.listdir(state_folder) if os.path.isfile(os.path.join(state_folder, f))])
        print(f"Number of images in {state_folder}: {image_count}")
        return image_count
    except Exception as e:
        print(f"Failed to count images in {state_folder}: {str(e)}")
        return 0


# List of state names
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
          "Georgia",
          "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
          "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
          "Pennsylvania",
          "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
          "Washington",
          "West Virginia", "Wisconsin", "Wyoming"]

# Iterate over each state
for state in states:
    # Folder path for the current state
    folder_path = f"sample_data/{state}"

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Call the count_images_in_state_folder function
        count_images_in_state_folder(folder_path)
    else:
        print(f"Folder does not exist: {folder_path}")
