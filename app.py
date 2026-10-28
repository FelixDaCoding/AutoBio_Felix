"""CSIT 349 - Autobiography and Portfolio App
Felix Kristian T. Ponce
"""
from datetime import date
import os

import numpy as np
import pandas as pd
import streamlit as st

# --------------------------------------------------------------------------
# Page setup
# --------------------------------------------------------------------------
NAME = "Felix Kristian T. Ponce"
SECTION = "F1"
EMAIL = "xtian1104@gmail.com"
PHONE = "09959943926"
BIRTHDAY = date(2005, 11, 4)

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="🎮",
    layout="wide",
)


def age_today() -> int:
    today = date.today()
    return today.year - BIRTHDAY.year - ((today.month, today.day) < (BIRTHDAY.month, BIRTHDAY.day))


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
SKILLS = pd.DataFrame(
    {
        "Skill": [
            "C Programming",
            "Data Structures",
            "Python",
            "Backend Development",
            "Game Idea & Design",
            "Teamwork",
            "Front-end / UI",
        ],
        "Category": [
            "Programming",
            "Programming",
            "Programming",
            "Development",
            "Game Dev",
            "Soft Skills",
            "Development",
        ],
        "Level": [75, 60, 65, 75, 90, 95, 40],
    }
)

MILESTONES = pd.DataFrame(
    {
        "When": ["1st year", "2nd year", "June 2026", "3rd year"],
        "Milestone": [
            "Learned to understand C code and started developing.",
            "Understood data structures and survived the year.",
            "Took part in a game jam.",
            "Built LevelUP, my capstone workout app, and this portfolio.",
        ],
    }
)

PROJECTS = {
    "LevelUP (Capstone)": {
        "icon": "💪",
        "image": "assets/levelup_capstone.jpg",
        "role": "Backend developer. I built the backend of our capstone workout app.",
        "tools": "JavaFX (used for the front end); [ME: backend language / database]",
        "outcome": "[https://github.com/FelixDaCoding/CAPSTONE-CSIT227-F2-TEAMPURA_TEST.git]",
        "details": "A workout app made as our capstone. I handled the backend while the front end was built with JavaFX. [EDIT ME: add 1-2 sentences on what the app does.]",
    },
    "Game Jam: Team Paulina (June 2026)": {
        "icon": "🕹️",
        "image": "assets/game_jam_paulina.png",
        "role": "Idea creator and backend developer. I usually leave the front end to teammates.",
        "tools": "[ME: Godot / languages used]",
        "outcome": "[https://github.com/donmerveilleu/Pauli.git] (team name: Paulina)",
        "details": "I joined a game jam in June 2026 as part of team Paulina. I came up with the game idea and handled the backend logic.",
    },
    "School Water Refilling Station (Concept)": {
        "icon": "💧",
        "image": "assets/water_refilling_station.png",
        "role": "Project creator. I came up with and developed the idea.",
        "tools": "[ME: used HTML,CSS, and Python and also Used Supabase as database]",
        "outcome": "A concept project that tackles a problem in school. It was not actually put into use.",
        "details": "A water refilling idea for our school, made as a class project to solve a real school problem. It is based on that problem and was never deployed or used in real life.",
    },
}

# --------------------------------------------------------------------------
# Session state
# --------------------------------------------------------------------------
if "hi_count" not in st.session_state:
    st.session_state.hi_count = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = []


# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------
def render_sidebar():
    with st.sidebar:
        if os.path.exists("assets/profile.jpg"):
            st.image("assets/profile.jpg", use_container_width=True)
        st.header(NAME)
        st.caption(f"CSIT 349 · Section {SECTION}")
        st.write("3rd year BS Computer Science")
        st.write(f"📧 {EMAIL}")
        st.write(f"📱 {PHONE}")
        st.divider()

        visitor = st.text_input("Your name", placeholder="Type your name")
        if st.button("👋 Say hi to Felix"):
            st.session_state.hi_count += 1
        if st.session_state.hi_count:
            who = visitor.strip() or "A visitor"
            st.success(f"{who} said hi! Total hellos: {st.session_state.hi_count}")

        st.divider()
        show_fun = st.checkbox("Show a fun fact", value=True)
        if show_fun:
            st.info("I'm a PC gamer, and I play a lot of games.")
        return visitor


# --------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------
def render_header(visitor: str):
    st.title(f"🎮 {NAME}")
    st.subheader("Aspiring software and game developer")
    if visitor.strip():
        st.write(f"Welcome, **{visitor.strip()}**! Thanks for visiting my page.")
    else:
        st.write("Hello Welcome To my AutoBiography!!!")
    st.divider()


def render_about():
    col_facts, col_text = st.columns([1, 2], gap="large")
    with col_facts:
        if os.path.exists("assets/profile.jpg"):
            st.image("assets/profile.jpg", caption=NAME, use_container_width=True)
        st.subheader("Quick facts")
        st.write("🎓 3rd year BS Computer Science")
        st.write("🏫 Cebu Institute of Technology - University")
        st.write("🎂 Born November 4, 2005")
        st.write("🎮 PC gamer")
        st.write("⚙️ Backend and game ideas")
    with col_text:
        st.header("About me")
        st.write(
            f"Hi, I'm **{NAME}**, a {age_today()}-year-old 3rd year BS Computer Science "
            "student at Cebu Institute of Technology - University. I love games, and I "
            "want to become a software developer or game developer who makes apps and "
            "games that many users can enjoy."
        )
        st.write(
            "When I work on games, I'm usually the one who comes up with the ideas and "
            "builds the backend. The front end is not my strong suit (I'm not great with "
            "sliders), so I team up with people who are."
        )
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Age", age_today())
        m2.metric("Year level", "3rd")
        m3.metric("Projects", len(PROJECTS))
        m4.metric("Game jams", 1)


def render_autobiography():
    st.header("My story")
    tab_bg, tab_edu, tab_int, tab_mile = st.tabs(
        ["🏠 Background", "🎓 Education", "🎯 Interests & Goals", "🏁 Milestones"]
    )

    with tab_bg:
        st.write(
            f"I was born on **November 4, 2005**. I grew up in a family of four, and I "
            "love them very much."
        )
        st.write(
            "My family went through hardships when I was growing up, and we worked our "
            "way up. Today we are living well. That experience taught me to value hard "
            "work and to stay grateful for the people beside me."
        )

    with tab_edu:
        st.write("**Cebu Institute of Technology - University**")
        st.write("BS Computer Science, currently in 3rd year.")
        st.write(
            "Overall, my school experience has been good, mostly because of the "
            "friends I've made along the way."
        )
        progress_year = st.slider("Degree progress (years completed of 4)", 0.0, 4.0, 2.0, 0.5, disabled=True)
        st.progress(progress_year / 4, text="I've finished 1st and 2nd year and I'm now in 3rd year.")

    with tab_int:
        st.write("**What I enjoy**")
        st.write("- 🖥️ PC gaming. I play a lot of games.")
        st.write("- 💡 Coming up with game ideas.")
        st.write("- ⚙️ Building the backend of apps and games.")
        st.write("**What I want to be**")
        st.write(
            "A software developer or game developer who creates apps and games that "
            "many users can play and enjoy."
        )

    with tab_mile:
        st.write("I survived 1st and 2nd year, and here's how it went:")
        st.table(MILESTONES.set_index("When"))


def render_skills():
    st.header("Skills")
    st.write(
        "My strongest areas are game ideas, backend work and teamwork. Front-end design "
        "is where I still have the most to learn."
    )

    col_filter, col_chart = st.columns([1, 2], gap="large")
    with col_filter:
        st.subheader("Filter")
        categories = st.multiselect(
            "Categories",
            sorted(SKILLS["Category"].unique()),
            default=sorted(SKILLS["Category"].unique()),
        )
        min_level = st.slider("Minimum level", 0, 100, 0, step=5)
        sort_by = st.radio("Sort by", ["Level (high to low)", "Skill name"], horizontal=True)

    filtered = SKILLS[SKILLS["Category"].isin(categories) & (SKILLS["Level"] >= min_level)]
    if sort_by == "Skill name":
        filtered = filtered.sort_values("Skill")
    else:
        filtered = filtered.sort_values("Level", ascending=False)

    with col_chart:
        st.subheader("Skill levels")
        if filtered.empty:
            st.warning("No skills match those filters.")
        else:
            st.bar_chart(filtered.set_index("Skill")["Level"])

    st.subheader("Skill table")
    if not filtered.empty:
        st.dataframe(
            filtered.reset_index(drop=True),
            column_config={
                "Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d")
            },
        )
        st.caption(f"Average level of shown skills: {np.mean(filtered['Level']):.1f}")


def render_projects():
    st.header("Projects")
    choice = st.selectbox("Pick a project", list(PROJECTS.keys()))
    show_details = st.checkbox("Show more details", value=True)

    p = PROJECTS[choice]
    col_a, col_b = st.columns([1, 1], gap="large")
    with col_a:
        st.subheader(f"{p['icon']} {choice}")
        st.write(f"**My role:** {p['role']}")
        st.write(f"**Tools:** {p['tools']}")
        st.write(f"**Outcome:** {p['outcome']}")
        if show_details:
            with st.expander("About this project", expanded=True):
                st.write(p["details"])
    with col_b:
        if "image" in p and os.path.exists(p["image"]):
            st.image(p["image"], caption=f"{choice} Preview", use_container_width=True)

    st.divider()
    st.caption("All projects")
    overview = pd.DataFrame(
        [{"Project": k, "My role": v["role"], "Tools": v["tools"]} for k, v in PROJECTS.items()]
    )
    st.dataframe(overview, hide_index=True)


def build_bio_text() -> str:
    lines = [
        f"# {NAME}",
        "3rd year BS Computer Science, Cebu Institute of Technology - University",
        f"Email: {EMAIL}",
        f"Phone: {PHONE}",
        "",
        "## Goal",
        "Software developer / game developer making apps and games for many users.",
        "",
        "## Milestones",
    ]
    for _, row in MILESTONES.iterrows():
        lines.append(f"- {row['When']}: {row['Milestone']}")
    lines += ["", "## Projects"]
    for title, p in PROJECTS.items():
        lines.append(f"- {title} - {p['role']}")
    return "\n".join(lines)


def render_contact():
    st.header("Contact & feedback")
    col_form, col_info = st.columns([2, 1], gap="large")

    with col_form:
        with st.form("feedback_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            message = st.text_area("Message or feedback")
            rating = st.slider("How did you like this page?", 1, 5, 4)
            submitted = st.form_submit_button("Send")

        if submitted:
            if not name.strip() or not message.strip():
                st.error("Please enter your name and a message.")
            else:
                st.session_state.feedback.append(
                    {"name": name.strip(), "email": email.strip(), "message": message.strip(), "rating": rating}
                )
                st.success(f"Thanks, {name.strip()}! Your message was received ({rating}/5 ⭐).")
                st.balloons()

    with col_info:
        st.subheader("Reach me")
        st.write(f"📧 {EMAIL}")
        st.write(f"📱 {PHONE}")
        st.download_button(
            "⬇️ Download my bio (.md)",
            data=build_bio_text(),
            file_name="felix_ponce_bio.md",
            mime="text/markdown",
        )
        if st.session_state.feedback:
            st.metric("Messages this session", len(st.session_state.feedback))


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
visitor_name = render_sidebar()
render_header(visitor_name)

tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["👤 About", "📖 Autobiography", "🛠️ Skills", "🚀 Projects", "✉️ Contact"]
)
with tab_about:
    render_about()
with tab_story:
    render_autobiography()
with tab_skills:
    render_skills()
with tab_projects:
    render_projects()
with tab_contact:
    render_contact()

st.divider()
st.caption(f"© {date.today().year} {NAME} · CSIT 349 Section {SECTION}")
