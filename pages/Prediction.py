import streamlit as st

from iris import predict_species


st.title("🌸 Iris Flower Prediction")

st.write(
    "Enter the measurements of an Iris flower "
    "to predict its species."
)

st.divider()


col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )


with col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )


st.divider()


if st.button("🔮 Predict Iris Species"):

    result = predict_species(
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    )

    st.success(
        f"🌺 Predicted Species: **{result}**"
    )