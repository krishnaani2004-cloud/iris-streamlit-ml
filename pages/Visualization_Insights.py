import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from iris import df


st.title("📊 Visualizations & Insights")

st.write(
    "Explore the Iris dataset through different "
    "visualizations and understand the important patterns."
)

st.divider()


# ------------------------------------------------
# 1. Species Distribution
# ------------------------------------------------

st.header("1️⃣ Species Distribution")

species_count = df["species"].value_counts()

st.bar_chart(species_count)

st.write("""
### Insight

The Iris dataset contains three species:

- Setosa
- Versicolor
- Virginica

Each species contains approximately the same number of samples,
making the dataset well balanced.
""")


st.divider()


# ------------------------------------------------
# 2. Feature Distribution
# ------------------------------------------------

st.header("2️⃣ Feature Distribution")

feature = st.selectbox(
    "Select a feature",
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

fig, ax = plt.subplots()

sns.histplot(
    data=df,
    x=feature,
    hue="species",
    kde=True,
    ax=ax
)

ax.set_title(f"Distribution of {feature}")

st.pyplot(fig)


st.divider()


# ------------------------------------------------
# 3. Scatter Plot
# ------------------------------------------------

st.header("3️⃣ Feature Relationship")

col1, col2 = st.columns(2)

with col1:

    x_feature = st.selectbox(
        "X-axis",
        [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ],
        index=0
    )


with col2:

    y_feature = st.selectbox(
        "Y-axis",
        [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ],
        index=2
    )


fig, ax = plt.subplots()

sns.scatterplot(
    data=df,
    x=x_feature,
    y=y_feature,
    hue="species",
    s=80,
    ax=ax
)

ax.set_title(
    f"{x_feature} vs {y_feature}"
)

st.pyplot(fig)


st.divider()


# ------------------------------------------------
# 4. Correlation
# ------------------------------------------------

st.header("4️⃣ Feature Correlation")

correlation = df[
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
].corr()

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

ax.set_title("Feature Correlation Matrix")

st.pyplot(fig)


st.divider()


# ------------------------------------------------
# 5. Important Insights
# ------------------------------------------------

st.header("💡 Key Insights")

st.success("""
### Insight 1
Petal length and petal width are highly useful features
for distinguishing Iris species.

### Insight 2
Iris Setosa is generally easier to separate from the
other two species.

### Insight 3
Versicolor and Virginica have more overlap compared
with Setosa.

### Insight 4
Petal measurements provide stronger separation between
species than many of the sepal measurements.
""")