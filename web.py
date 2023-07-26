import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" #here the session state is a kind of a dictionary that will grab the input text using the key new_todo
    todos.append(todo)
    functions.write_todos(todos)


st.title("My to-do App")
st.subheader("This is my to-do app")
st.write("this app is to increase your creativity")

for index, todo in enumerate(todos):  #here this will iterate over the txt file - todos.txt
    checkbox = st.checkbox(todo, key=todo)  # a key will be implement as each checkbox must have a different key toebe able to be deleted
    if checkbox:  #if this is true - if checkbox is ticked then
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  #this will delete the session state related to the deleted key
        st.experimental_rerun()

st.text_input(label="enter a todo", placeholder="Add a new todo..",
              on_change=add_todo, key='new_todo')  #here the label is a requirement -

# in order to upload this project on the cloud we need to run the following command on the terminal
# pip freeze > requirements.txt
#this command will get all the packages required in order to run the app on the cloud

#to run the app on the local server and test it, apply the following command on the terminal: streamlit run web.py