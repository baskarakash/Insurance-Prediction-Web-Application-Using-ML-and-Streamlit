import streamlit as st
from joblib import load

# Load the model
model = load("insur.joblib")

def main():
    # Set page layout and colors
    st.set_page_config(
        page_title="Insurance Prediction App",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Define custom CSS for colorful theme with contrasting background
    st.markdown(
        """
        <style>
        .custom-bg {
            background-color: #f8f9fa !important; /* Light gray for contrast */
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 8px 12px;
            font-size: 16px;
            box-sizing: border-box;
            width: 100%;
        }
        .stNumberInput>div>div>div>input {
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 8px 12px;
            font-size: 16px;
            box-sizing: border-box;
            width: 100%;
        }
        .stRadio>div>label {
            color: white;
            border-radius: 5px;
            padding: 8px 12px;
            margin-right: 5px;
        }
        .stRadio>div>div>span {
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Apply custom background class to the body element
    st.markdown('<body class="custom-bg">', unsafe_allow_html=True)

    # Main title
    st.title("Insurance Prediction App")

    # Secondary heading
    st.subheader("Fill in the following details to get your insurance prediction.")

    # Input details section
    st.markdown("---")
    st.header("Enter Your Details")

    # Create a container for input fields
    input_container = st.container()

    with input_container:
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=0, max_value=100, step=1, value=30)
            bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, value=25.0)
            smoker = st.selectbox("Smoker", options=["No", "Yes"])
        with col2:
            sex = st.radio("Gender", options=["Male", "Female"])
            children = st.number_input("Number of Children", min_value=0, max_value=10, step=1, value=0)

    # Convert selected options to numerical values
    sex = 1 if sex == "Male" else 0
    smoker = 1 if smoker == "Yes" else 0

    # Prediction button
    st.markdown("---")
    if st.button("Get Prediction"):
        # Predict insurance cost
        prediction = model.predict([[age, sex, bmi, children, smoker]])
        st.write("Predicted Insurance Cost: $", round(prediction[0], 2))

if __name__ == "__main__":
    main()
