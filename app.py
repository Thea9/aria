import streamlit as st

# Title and Introduction
st.title("ARIA: Arts & Recreation Interaction Advisor")
st.markdown("""
**ARIA (Arts & Recreation Interaction Advisor)** nurtures each homeschool student's creative passions by:
- Identifying artistic interests (painting, photography, crafting).
- Recommending age-appropriate projects and classes.
- Curating virtual art galleries, online critique circles, and local workshops.
- Coordinating arts-based contests (e.g., "Monthly Photo Spotlight") with SIMON.
""")

# Sidebar for user inputs
st.sidebar.header("Student's Artistic Interests")
interests = st.sidebar.multiselect(
    "Select student interests:",
    ["Painting", "Photography", "Crafting", "Digital Art", "Music"]
)

st.sidebar.header("Student's Age Group")
age_group = st.sidebar.selectbox(
    "Select age group:",
    ["Under 8", "8-12", "13-17", "18+"]
)

# Button to generate ARIA's recommendations
if st.sidebar.button("Get ARIA's Recommendations"):
    st.subheader("ARIA's Creative Recommendations")

    # Project and Class Recommendations
    st.markdown("**Recommended Projects & Classes:**")
    if "Painting" in interests:
        if age_group in ["Under 8", "8-12"]:
            st.write("- Watercolor basics: Follow a simple watercolor tutorial suitable for ages 8-12.")
            st.write("- Local kids' painting workshop at the community art center.")
        else:
            st.write("- Acrylic painting course: Learn advanced techniques in local studios.")
            st.write("- Online figure drawing class for teens and adults.")
    if "Photography" in interests:
        if age_group in ["Under 8", "8-12"]:
            st.write("- Beginner photography scavenger hunt: Capture simple household items.")
            st.write("- Virtual workshop: Photography Fun for Kids.")
        else:
            st.write("- Online composition and lighting class for teens/adults.")
            st.write("- Local youth photography club meetup every Saturday.")
    if "Crafting" in interests:
        if age_group in ["Under 8", "8-12"]:
            st.write("- DIY clay modeling project: Mold simple figurines at home.")
            st.write("- Local kids' crafting hour at the library.")
        else:
            st.write("- Advanced paper quilling workshop for teens/adults.")
            st.write("- Online jewelry-making class.")
    if "Digital Art" in interests:
        if age_group in ["Under 8", "8-12"]:
            st.write("- Simple digital drawing app tutorials for beginners.")
            st.write("- Virtual cartoon sketching class.")
        else:
            st.write("- Digital illustration bootcamp for teens/adults.")
            st.write("- Online character design workshop.")
    if "Music" in interests:
        if age_group in ["Under 8", "8-12"]:
            st.write("- Intro to keyboard for kids: Learn basic notes and songs.")
            st.write("- Virtual singing circle for young beginners.")
        else:
            st.write("- Online guitar theory and practice for teens/adults.")
            st.write("- Local youth orchestra open rehearsals.")

    st.markdown("---")
    # Curated Virtual Galleries and Workshops
    st.markdown("**Curated Virtual Galleries & Workshops:**")
    if set(interests) & {"Painting", "Photography", "Crafting"}:
        st.write("- Monthly Virtual Art Gallery: Submit your art/photography to be showcased online.")
        st.write("- Online critique circle: Join peers in giving and receiving feedback on artwork.")
    if "Digital Art" in interests:
        st.write("- Digital Art Exhibition: Display digital pieces in a virtual gallery.")
    if interests:
        st.write("- Local workshop schedule: Check community center listings for upcoming classes.")

    st.markdown("---")
    # Arts-Based Contests
    st.markdown("**Upcoming Arts-Based Contests:**")
    st.write("- **Monthly Photo Spotlight:** Submit your best photograph; winners get featured in the virtual gallery.")
    st.write("- **Seasonal Painting Challenge:** Create a painting based on seasonal themes; judged by local artists.")
    st.write("- **Crafting Corner Contest:** Craft a DIY project and share photos for peer voting.")

else:
    st.info("Select interests and age group in the sidebar, then click 'Get ARIA's Recommendations' to begin.")
