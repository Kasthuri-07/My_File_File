import streamlit as st
st.title("Vinsup Application")
st.header("software")
st.subheader("30 days")
st.metric("python", 10, -12)
st.write("❤️Kasthuri kumar❤️")
st.write("_Kasthuri kumar_")
st.write("- Kasthuri kumar")
st.write("# Kasthuri kumar")
st.write("### Kasthuri kumar")

st.divider()

st.sidebar.header("My sidebar")
st.sidebar.button("get start")
st.sidebar.text_input("Name")
st.code("""# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))



""",language="python")
st.slider("Age",0,100)
st.date_input("DOB")


st.divider()
st.text_input("Student Name")
st.number_input("Phone Number")
st.selectbox("city",options=["Madurai","Chennai","dindigul"])
st.radio("Gender",options=["Male","Female"])
st.multiselect("Skills",options=["HTML","css","java","js"])