import streamlit as st
import requests

# Define a function to serve the FastAPI endpoint via Streamlit
def serve_fastapi():
    st.title("Credit Score Prediction")

    person_age_bin = st.text_input("Person Age (Numeric)")
    person_income_bin = st.text_input("Person Income (Numeric)")
    person_emp_length_bin = st.text_input("Person Employment Length (Numeric)")
    loan_amnt_bin = st.text_input("Loan Amount (Numeric)")
    loan_int_rate_bin = st.text_input("Loan Interest Rate (From 5.5 to 22%)")
    loan_percent_income_bin = st.text_input("Loan Percent of Income (From 0.09 to 0.83)")
    cb_person_cred_hist_length_bin = st.text_input("Credit History Length (From 2 to 30)")
    person_home_ownership = st.selectbox("Person Home Ownership", ["OWN", "MORTGAGE", "RENT", "OTHER"])
    loan_intent = st.selectbox("Loan Intent", ["EDUCATION", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
    loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
    cb_person_default_on_file = st.selectbox("Credit Default on File", ["Y", "N"])

    if st.button("Predict Credit Score"):
        input_data = {
            "person_age_bin": int(person_age_bin),
            "person_income_bin": int(person_income_bin),
            "person_emp_length_bin": int(person_emp_length_bin),
            "loan_amnt_bin": int(loan_amnt_bin),
            "loan_int_rate_bin": int(loan_int_rate_bin),
            "loan_percent_income_bin": float(loan_percent_income_bin),
            "cb_person_cred_hist_length_bin": int(cb_person_cred_hist_length_bin),
            "person_home_ownership": person_home_ownership,
            "loan_intent": loan_intent,
            "loan_grade": loan_grade,
            "cb_person_default_on_file": cb_person_default_on_file
        }

        # Send a POST request to your FastAPI endpoint
        response = requests.post("https://creditscorecard-670abc4179ee.herokuapp.com/predict_score", json=input_data)

        # Check if the response is successful
        if response.status_code == 200:
            try:
                result = response.json()
                st.success(f"Credit Score: {result['Credit Score']}")
            except ValueError:
                st.error("Invalid response from the server.")
        else:
            st.error("Error: Unable to fetch results from the server.")

if __name__ == "__main__":
    serve_fastapi()
