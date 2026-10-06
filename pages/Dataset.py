import streamlit as st

from iris import df


st.title("📋 Iris Dataset")

st.write(
    "Explore the complete Iris dataset."
)

st.divider()


# Dataset preview
st.header("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)


st.divider()


# Dataset information
st.header("📌 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Rows",
        df.shape[0]
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Missing Values",
        df.isnull().sum().sum()
    )


st.divider()


# Statistics
st.header("📈 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)


st.divider()


# Species counts
st.header("🌺 Species Count")

st.write(
    df["species"].value_counts()
)