import streamlit as st

st.set_page_config(
    page_title="Crowd Detection",
    layout="centered"
)

st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "How to Use", "About"]
)

if page == "Home":
    st.title("Crowd Detection System")
    st.write("Upload an image or video to detect people.")

    uploaded_file = st.file_uploader(
        "Upload Image or Video",
        type=["jpg", "png", "mp4"]
    )

    if uploaded_file:
        st.success("File uploaded successfully!")

        if uploaded_file.type.startswith("image"):
            st.image(uploaded_file)
        else:
            st.video(uploaded_file)

        if st.button("Run Detection"):
            st.info("Running model...")
            # nanti model temen kamu masuk di sini
            st.success("Detection completed!")
            st.metric("Total People Detected", 12)

elif page == "How to Use":
    st.title("How to Use")
    st.markdown("""
    **Steps:**
    1. Upload image (.jpg, .png) or video (.mp4)
    2. Click **Run Detection**
    3. View detection result and total count
    """)

elif page == "About":
    st.title("About This Project")
    st.write("""
    This project aims to detect and count people in images or videos
    to support crowd monitoring and safety analysis.
    """)
