import streamlit as st

st.title("BMI Calculator")
name = st.text_input("Enter your name: ", placeholder = "Type your name here...")
height = st.number_input("Enter your height in cm: ", min_value = 50, max_value = 250)
weight = st.number_input("Enter your weight in kg: ", min_value = 1, max_value = 300)

if st.button("Calculate BMI"):
    bmi = weight/(height/100)**2
    st.write(f"{name}, your BMI is: {bmi:.2f}")
    
    st.progress(min(int(bmi), 100))
    st.write(f"BMI Progress: {bmi:.1f}/100")
    
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        st.success("You have a normal weight.")
    elif bmi >=25.0 and bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
st.image("https://unsplash.com/photos/a-group-of-women-running-on-a-road-next-to-a-body-of-water-AdVrlzyHcxQ")