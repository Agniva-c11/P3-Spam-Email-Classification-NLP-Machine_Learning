import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vect.pkl', 'rb'))

def main():
    st.title("Email Spam Classification Application")
    st.write("This is a machine learning application to classify emails as spam or not spam.")
    
    st.subheader("Classification")
    user_input = st.text_area("Enter an email to classify:", height=150)
    
    if st.button("Classify"):
        if user_input:
            data = [user_input]
            st.write(f"Input data: {data}")  # For debugging, shows user input
            try:
                vec = cv.transform(data).toarray()
                result = model.predict(vec)
                if result[0] == 0:
                    st.success("This is not a Spam Email")
                else:
                    st.error("This is a Spam Email")
            except Exception as e:
                st.error(f"An error occurred during classification: {e}")
        else:
            st.warning("Please, enter an email to classify.")

main()
