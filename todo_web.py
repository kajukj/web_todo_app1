import streamlit as st
import todo_function as fun

st.title("My Todo App")
st.subheader("Todo List")

todos = fun.get_todo("todos.txt")
def add_todo():
    todo = st.session_state["add"]+"\n"
    todos.append(todo)
    fun.write_todo(todos)
    st.session_state["add"] = ""

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo,key="add")

