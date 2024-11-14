import streamlit as st
import requests
import json

BASE_URL = "http://127.0.0.1:5000"


def main():
    # Set the title and description for the app
    st.title("🌟 Rule Engine GUI 🌟")

    st.markdown(
        """
        <h2 style='color: #007BFF; font-weight: bold;'>Description of the Rule Engine</h2>
        <p>The Rule Engine application allows users to create, combine, evaluate, and modify rules easily through a user-friendly interface. This tool is essential for automating decision-making processes based on predefined rules.</p>

        <h2 style='color: #007BFF; font-weight: bold;'>How We Made It</h2>
        <p>We developed this application using Python and integrated the Flask web framework for the backend, providing endpoints to manage rules effectively. The frontend is built using Streamlit, allowing for a seamless user experience.</p>

        <h2 style='color: #007BFF; font-weight: bold;'>Why We Made It</h2>
        <p>The goal of this application is to simplify the process of rule management for users, making it accessible even for those with limited technical knowledge. By streamlining this process, we enhance productivity and decision-making capabilities.</p>
        """
    )

    st.markdown("<h2 style='color: #007BFF; font-weight: bold;'>Navigate to the Rule Engine</h2>",
                unsafe_allow_html=True)
    if st.button("Open Rule Engine"):
        st.session_state.page = "rule_engine"
        st.experimental_rerun()

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "rule_engine":
        rule_engine_interface()


def rule_engine_interface():
    st.header("Rule Engine Interface")

    # Create Rule Section
    rule_string = st.text_input("Create Rule")
    if st.button("Create Rule"):
        create_rule(rule_string)

    # Combine Rules Section
    rule_ids = st.text_input("Combine Rules (comma-separated IDs)")
    if st.button("Combine Rules"):
        combine_rules(rule_ids)

    # Evaluate Rule Section
    mega_rule_id = st.text_input("Evaluate Rule (Rule ID)")
    data = st.text_area("Data (JSON)")
    if st.button("Evaluate Rule"):
        evaluate_rule(mega_rule_id, data)

    # Modify Rule Section
    modify_rule_id = st.text_input("Modify Rule (Rule ID)")
    new_rule_string = st.text_input("New Rule String")
    if st.button("Modify Rule"):
        modify_rule(modify_rule_id, new_rule_string)


def create_rule(rule_string):
    try:
        response = requests.post(f"{BASE_URL}/create_rule", json={"rule_string": rule_string})
        response.raise_for_status()
        st.success(f"Create Rule Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


def combine_rules(rule_ids):
    rule_ids = [id.strip() for id in rule_ids.split(',')]
    try:
        response = requests.post(f"{BASE_URL}/combine_rules", json={"rule_ids": rule_ids})
        response.raise_for_status()
        st.success(f"Combine Rules Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


def evaluate_rule(mega_rule_id, data):
    try:
        data_json = json.loads(data)
        response = requests.post(f"{BASE_URL}/evaluate_rule", json={"rule_id": mega_rule_id, "data": data_json})
        response.raise_for_status()
        st.success(f"Evaluate Rule Response: {response.json()}")
    except json.JSONDecodeError as e:
        st.error(f"JSON Decode Error: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


def modify_rule(rule_id, new_rule_string):
    try:
        response = requests.post(f"{BASE_URL}/modify_rule",
                                 json={"rule_id": rule_id, "new_rule_string": new_rule_string})
        response.raise_for_status()
        st.success(f"Modify Rule Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
