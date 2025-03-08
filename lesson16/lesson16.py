import streamlit as st



def main():
    st.title('Hello World')

if __name__ == '__main__':
  main()

if st.button("Click Me!"):
    st.write("Button clicked")

st.checkbox("Check Me!")

if st.checkbox("Click me to show some text"):
    st.write("You are seeing this because you clicked the button")

user_input = st.text_input("Text here", "Shenoni nje text")
st.write("You texted:", user_input)

age = st.number_input("Text here",min_value=1,max_value=100)
st.write(f"Your age: {age} ")

message = st.text_area("Text here")
st.write(f"You typed : {message}")

choice = st.radio("Chose one", ['Choice 1','Choice 2','Choice 3'])
st.write(f"You chose {choice}")

if st.button("Success"):
   st.success("It was successfull")

try:
 1 / 0
except Exception as e:
 st.write()

