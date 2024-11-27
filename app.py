import streamlit as st
import requests

# Title of the app
st.title("Random Dog Images")

# API URL
dog_api_url = "https://dog.ceo/api/breeds/image/random"

# Fetch a dog image when the button is clicked
if st.button("Get Random Dog Image"):
    try:
        # Make the API request
        response = requests.get(dog_api_url)
        data = response.json()

        # Check for success status in the response
        if response.status_code == 200 and data["status"] == "success":
            # Display the image
            st.image(data["message"], caption="Random Doggo!", use_container_width=True)
        else:
            st.error("Failed to fetch a valid response from the API.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# List of available breeds
breeds_url = "https://dog.ceo/api/breeds/list/all"
breeds_response = requests.get(breeds_url).json()
breed_list = list(breeds_response["message"].keys())

# Dropdown for selecting breed
selected_breed = st.selectbox("Select a Dog Breed", breed_list)

if st.button("Get Breed Images"):
    try:
        breed_url = f"https://dog.ceo/api/breed/{selected_breed}/images/random/3"  # Get 3 images of the breed
        breed_response = requests.get(breed_url).json()
        if breed_response["status"] == "success":
            for img_url in breed_response["message"]:
                st.image(img_url, caption=f"A {selected_breed.capitalize()}!", use_container_width=True)
        else:
            st.error("Failed to fetch images for the selected breed.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


