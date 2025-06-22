import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from streamlit_lottie import st_lottie
import json
import requests

# Configuration de la page
st.set_page_config(
    page_title="CV Ingénieur en Statistique et Informatique Décisionnelle",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fonction pour charger les animations Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animations Lottie
lottie_data = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vybwn7df.json")
lottie_skills = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_1a8xe7is.json")
lottie_contact = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_u25cckyh.json")

# CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Barre latérale avec photo et info contact
with st.sidebar:
    st.markdown("""
    <div style="text-align:center">
        <img src="https://i.imgur.com/7X8XrQq.png" alt="Photo Profil" width="150" style="border-radius:50%; margin-bottom:20px;">
        <h2>Ingénieur en Statistique et Informatique Décisionnelle</h2>
        <p>Votre expert en données pour des décisions éclairées</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    with st.expander("📩 Contact", expanded=True):
        st.markdown("""
        **📧 Email**  
        votre.email@example.com  
        
        **📞 Téléphone**  
        +33 X XX XX XX XX  
        
        **📍 Localisation**  
        Paris, France  
        """)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align:center">
        <h4>Réseaux Professionnels</h4>
        <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30"/></a>
        <a href="#"><img src="https://img.icons8.com/color/48/000000/github.png" width="30"/></a>
        <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" width="30"/></a>
    </div>
    """, unsafe_allow_html=True)

# Contenu principal
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Accueil", "🛠️ Compétences", "💼 Expériences", "📚 Formation", "📞 Contact"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="text-align:left">
            <h1 style="color:#2a79b7; font-size:2.5em;">Bonjour, Je suis [Votre Prénom]</h1>
            <h2 style="color:#333; font-size:1.8em;">Ingénieur en Statistique et Informatique Décisionnelle</h2>
            <p style="font-size:1.1em; line-height:1.6;">
                Je suis un ingénieur spécialisé en analyse de données et modélisation, avec plus de 5 ans d'expérience 
                dans la résolution de problématiques complexes liées aux données. Mon expertise couvre les statistiques 
                appliquées et l'informatique décisionnelle, me permettant de transformer des données brutes en informations 
                stratégiques.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Statistiques clés
        st.markdown("### 📈 Mes Chiffres Clés")
        col1, col2, col3 = st.columns(3)
        col1.metric("Années d'Expérience", "5+", "3 secteurs")
        col2.metric("Projets Réalisés", "50+", "12 clients")
        col3.metric("Modèles Déployés", "30+", "en production")
        
    with col2:
        if lottie_data:
            st_lottie(lottie_data, height=300, key="data")
        
        # Simulation de compétences avec un graphique radar
        st.markdown("### 🎯 Profil Compétences")
        categories = ['Analyse', 'Modélisation', 'Programmation', 'Communication', 'Gestion']
        fig = px.line_polar(
            r=[9, 8, 9, 7, 6], 
            theta=categories, 
            line_close=True,
            template="plotly_dark",
            color_discrete_sequence=["#2a79b7"]
        )
        fig.update_traces(fill='toself')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("## 🛠️ Mes Compétences Techniques")
    
    if lottie_skills:
        st_lottie(lottie_skills, height=200, key="skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Analyse de Données")
        st.progress(90)
        st.markdown("""
        - Analyse multidimensionnelle et multivariée
        - Data mining et exploration
        - Statistiques descriptives et inférentielles
        - Visualisation de données
        """)
        
        st.markdown("### 🤖 Modélisation Prédictive")
        st.progress(85)
        st.markdown("""
        - Régression et classification
        - Séries temporelles
        - Optimisation statistique
        - Validation de modèles
        """)
    
    with col2:
        st.markdown("### 💻 Programmation")
        st.progress(95)
        st.markdown("""
        - Python (Pandas, NumPy, Scikit-learn)
        - R (Tidyverse, Shiny)
        - SAS (Base, Macro)
        - SQL avancé
        """)
        
        st.markdown("### 📝 Enquêtes & Communication")
        st.progress(80)
        st.markdown("""
        - Conception de questionnaires
        - Analyse d'enquêtes
        - Rédaction de rapports
        - Présentation à des non-experts
        """)
    
    st.markdown("---")
    
    st.markdown("## 🛠️ Outils et Technologies")
    tools = {
        "Langages": ["Python", "R", "SAS", "SQL"],
        "Data Science": ["Pandas", "NumPy", "Scikit-learn", "TensorFlow"],
        "Visualisation": ["Matplotlib", "Seaborn", "Plotly", "Tableau"],
        "Bases de Données": ["PostgreSQL", "MySQL", "MongoDB", "Snowflake"]
    }
    
    for category, items in tools.items():
        with st.expander(f"📌 {category}"):
            cols = st.columns(4)
            for i, item in enumerate(items):
                cols[i].markdown(f"- {item}")

with tab3:
    st.markdown("## 💼 Expériences Professionnelles")
    
    # Timeline des expériences
    exp_data = [
        {"title": "Prévention de Fraudes Bancaires", 
         "date": "2020 - Présent", 
         "desc": "Développement de modèles sophistiqués pour détecter et prévenir la fraude, réduisant les pertes financières de 30%."},
        {"title": "Audit et Évaluation de Risques", 
         "date": "2018 - 2020", 
         "desc": "Réalisation d'audits détaillés et évaluation des risques pour des entreprises du secteur de l'assurance."},
        {"title": "Encadrement d'Équipe", 
         "date": "2017 - 2018", 
         "desc": "Gestion et mentorat d'une équipe de 3 statisticiens juniors, assurant la montée en compétences."}
    ]
    
    for exp in exp_data:
        with st.container():
            st.markdown(f"### {exp['title']}")
            st.caption(f"📅 {exp['date']}")
            st.markdown(exp['desc'])
            st.markdown("---")
    
    st.markdown("## 🚀 Projets Réalisés")
    
    # Cartes de projets
    projects = [
        {"name": "Tableau de Bord Interactif", "desc": "Conception d'un tableau de bord dynamique pour la visualisation des KPIs."},
        {"name": "Scoring Client (Banque)", "desc": "Implémentation d'une solution de scoring client pour l'attribution de crédits."},
        {"name": "Optimisation de Production", "desc": "Optimisation du plan de production par simulation statistique."}
    ]
    
    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i]:
            with st.expander(f"📌 {project['name']}"):
                st.markdown(project['desc'])
                st.button("Voir Détails", key=f"project_{i}")

with tab4:
    st.markdown("## 📚 Formation et Diplômes")
    
    # Graphique de formation
    education = [
        {"degree": "Ingénieur en Statistique", "year": "2015 - 2018", "score": 100},
        {"degree": "Analyse Numérique", "year": "2014", "score": 95},
        {"degree": "Cours Fondamentaux", "year": "2013 - 2015", "score": 90}
    ]
    
    for edu in education:
        st.markdown(f"### {edu['degree']}")
        st.caption(f"📅 {edu['year']}")
        st.progress(edu['score'])
        st.markdown("""
        - Algèbre linéaire avancée
        - Probabilités et statistiques
        - Data mining et machine learning
        - Informatique décisionnelle
        """)
        st.markdown("---")

with tab5:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("## 📞 Contactez-moi")
        if lottie_contact:
            st_lottie(lottie_contact, height=200, key="contact")
        
        st.markdown("""
        **📧 Email**  
        votre.email@example.com  
        
        **📞 Téléphone**  
        +33 X XX XX XX XX  
        
        **📍 Localisation**  
        Paris, France  
        """)
        
        st.markdown("""
        <div style="margin-top:20px">
            <h4>Réseaux Professionnels</h4>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30"/></a>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/github.png" width="30"/></a>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" width="30"/></a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("## ✉️ Envoyez-moi un message")
        
        with st.form("contact_form"):
            name = st.text_input("Nom Complet*")
            email = st.text_input("Email*")
            subject = st.text_input("Sujet*")
            message = st.text_area("Message*", height=150)
            
            # Bouton avec style personnalisé
            st.markdown("""
            <style>
                .stButton>button {
                    background-color: #2a79b7;
                    color: white;
                    border: none;
                    padding: 10px 24px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                    transition: all 0.3s;
                }
                .stButton>button:hover {
                    background-color: #1e5a8a;
                    transform: scale(1.02);
                }
            </style>
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button("Envoyer le Message")
            if submitted:
                if name and email and subject and message:
                    with st.spinner("Envoi en cours..."):
                        time.sleep(2)
                        st.success("Message envoyé avec succès! Je vous répondrai dans les plus brefs délais.")
                else:
                    st.error("Veuillez remplir tous les champs obligatoires (*)")

# Pied de page
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding:20px 0">
    <p>© 2023 Ingénieur en Statistique et Informatique Décisionnelle. Tous droits réservés.</p>
</div>
""", unsafe_allow_html=True)
