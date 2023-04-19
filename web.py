import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(page_title="Jei Cohen - Python Todos App")


def add_todo():
    todos.append(st.session_state["new_todo"] + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''


st.title("My Python Todo App")
st.subheader("This is my todo app.")
st.write("This app is to <b>increase</b> your productivity.",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label_visibility="hidden", label="todo-label",
              placeholder="Add new ToDo...", on_change=add_todo, key='new_todo')

