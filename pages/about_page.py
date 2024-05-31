import streamlit as st

def main():
    st.title("About Us")
    with st.sidebar:
        st.header('🧭 Navigation')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link('pages/about_page.py', label='About our team', icon='🌟')
        st.page_link('pages/contact_page.py', label='Contact us', icon='📧')
        st.page_link('pages/help_page.py', label='Help', icon='❓')
        st.markdown('---')

    # Define team members with their details
    team_members = [
        {
            "name": "Achraf Majidi",
            "role": "Team Lead",
            "bio": "Experienced software engineer with a focus on AI.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_jt1yw30l24.jpg&w=256&q=75"
        },
        {
            "name": "Oussama OUZAKRI",
            "role": "Sofware engineering student",
            "bio": "Passionate software engineering student who wants to develop his AI skills.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_l81tdp0w2m.jpg&w=96&q=75"
        },
        {
            "name": "Abdessamad Anssem",
            "role": "Sofware engineering student",
            "bio": "Passionate by AI and ML",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_xd2acu020r.jpg&w=96&q=75"
        },
        {
            "name": "Ali Mouna",
            "role": "Data engineering student",
            "bio": "Enthusiast data engineering student by AI.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_ac8qy0xef.jpg&w=256&q=75"
        },
        {
            "name": "Afsheen Ghuman",
            "role": "Laravel Developer at Eazisols",
            "bio": "Laravel and python developer",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_k259um0wni.jpg&w=96&q=75"
        },
        {
            "name": "Irtaza Zafar",
            "role": "Software Engineer",
            "bio": "I have been following and interested in many technologies such as AI, Web Development, Mobile App Development and Game Development Unity.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_5m7n0a0dqo.jpg&w=96&q=75"
        }
    ]

    # Display team members vertically with circular images
    for member in team_members:
        st.image(member['image_url'], width=96, caption=member['role'], use_column_width=False, output_format="JPEG",)
        st.write(f"**{member['name']}**")
        st.write(member['bio'])
        st.markdown('---')

if __name__ == "__main__":
    main()