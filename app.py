import streamlit as st
from iris import df, accuracy

st.set_page_config(
    page_title="Iris ML App",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 Iris Flower Machine Learning App")

st.subheader("Welcome to the Iris Flower Prediction System")

st.write("""
This Streamlit application uses Machine Learning to classify
Iris flowers into three different species.
""")

st.divider()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Samples",
        len(df)
    )

with col2:
    st.metric(
        "Features",
        4
    )

with col3:
    st.metric(
        "Model Accuracy",
        f"{accuracy * 100:.2f}%"
    )

st.divider()

st.header("🌺 Iris Species")

st.write("""
The Iris dataset contains three species:

- 🌸 **Iris Setosa**
- 🌺 **Iris Versicolor**
- 🌷 **Iris Virginica**

The prediction is based on four measurements:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width
""")

st.info(
    "Use the sidebar to navigate to Prediction, "
    "Visualization & Insights, and Dataset pages."
)