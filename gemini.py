import streamlit as st

def create_profile_update_form():
  """
  Creates a Streamlit form for updating user profile data.
  """
  with st.form("profile_update"):
    full_name = st.text_input(label="Full Name")
    course = st.text_input(label="Course")
    branch = st.text_input(label="Branch")
    batch = st.text_input(label="Batch")
    submit_button = st.button("Update Profile")

  if st.form_submitted("profile_update"):
    # Replace this with your logic to handle form submission
    # - Access submitted data using variables like full_name, course, etc.
    # - Update your database (replace `# ...` with your update logic)
    st.success("Profile update successful!")
    # Optionally, reset form fields after successful update
    st.session_state["profile_update"] = {}  # Reset form state

# ... your other application code 

# Call the function to create the form
create_profile_update_form()
