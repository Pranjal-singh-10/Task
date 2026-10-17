
import streamlit as st

st.title("To-Do List")

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

def add_task():
    task = st.session_state.task_input.strip()
    if task:
        st.session_state["task_list"].append(task)
    st.session_state.task_input = ""

def remove_task(task): st.session_state["task_list"].remove(task)

st.text_input("Enter your task", key="task_input")

st.button("Add Task", on_click=add_task)

for i, t in enumerate(st.session_state["task_list"]):
    if st.checkbox(t, key=f"task_{i}"):
        st.session_state["task_list"].remove(t)
        st.rerun()

