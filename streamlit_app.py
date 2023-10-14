# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection(
    "local_db",
    type="sql",
    url="mysql://root:ogre0382@localhost:3306/pets"
)

# Perform query.
df = conn.query('SELECT * from mytable;')

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
