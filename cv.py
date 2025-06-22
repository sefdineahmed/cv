import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge

# Configuration de la page
st.set_page_config(
    page_title="CV – Ingénieur Data",
    page_icon="📊",
    layout="wide"
)

# Bannière d’accueil
st.markdown(
    "<h1 style='text-align: center; color: #2C3E50;'>📊 Ingénieur en Statistique & Informatique Décisionnelles</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center; color: #7F8C8D;'>Votre expert en données pour des décisions éclairées</h4><br>",
    unsafe_allow_html=True
)

# Colonnes pour à propos
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
with col2:
    st.subheader("À propos de moi")
    st.markdown("""
    👨‍💻 Je suis un ingénieur spécialisé en **analyse de données et modélisation**, avec plus de **5 ans d'expérience**.

    ✅ Mon expertise couvre :
    - Les **statistiques appliquées**
    - L’**informatique décisionnelle**
    - Le **traitement de données complexes**
    
    💡 Je transforme les données en **informations stratégiques** pour accompagner la prise de décision.
    """)

st.markdown("---")

# Compétences Clés
st.subheader("🔧 Compétences Clés")
cols = st.columns(3)
competences = {
    "📊 Analyse de Données": "Multidimensionnelle & multivariée",
    "🤖 Modélisation Prédictive": "Optimisation des processus métiers",
    "💻 Programmation": "R, Python, SAS",
    "📋 Enquêtes & Questionnaires": "Conception & traitement",
    "🗣️ Communication": "Vulgarisation des résultats"
}
for i, (titre, desc) in enumerate(competences.items()):
    with cols[i % 3]:
        st.markdown(f"**{titre}**  \n{desc}")

st.markdown("---")

# Expériences
st.subheader("💼 Expériences Professionnelles")
exp = {
    "🛡️ Prévention de Fraudes": "Détection de fraudes bancaires via des modèles prédictifs",
    "📉 Audit & Risques": "Évaluation des risques pour des compagnies d'assurance",
    "👨‍🏫 Encadrement d'équipe": "Gestion et mentorat de 3 statisticiens",
    "📊 Rapports Décisionnels": "Création de dashboards clairs pour la direction"
}
for titre, desc in exp.items():
    st.markdown(f"- **{titre}** : {desc}")

st.markdown("---")

# Projets
st.subheader("🚀 Projets Réalisés")
projects = [
    "📈 **Tableau de Bord Interactif** – Suivi de KPIs",
    "💳 **Scoring Client (Banque)** – Attribution de crédits",
    "🏭 **Optimisation de Production** – Simulation statistique",
    "🛒 **Étude de Satisfaction Clients** – Recommandations stratégiques"
]
for p in projects:
    st.markdown(f"- {p}")

st.markdown("---")

# Formation
st.subheader("🎓 Formation & Diplômes")
col1, col2, col3 = st.columns(3)
with col1:
    st.progress(1.0, "Diplôme d’ingénieur en Statistique")
with col2:
    st.progress(0.95, "Certificat Analyse Numérique")
with col3:
    st.progress(0.90, "Cours Fondamentaux (data mining, proba...)")

st.markdown("---")

# Outils & Technologies
st.subheader("🧰 Outils et Technologies")
st.markdown("""
- Langages : **Python**, **R**, **SAS**, SQL  
- Visualisation : **Power BI**, **Tableau**, **Matplotlib**, **Seaborn**  
- Machine Learning : **scikit-learn**, **XGBoost**, **Statsmodels**  
- Base de données : **PostgreSQL**, **MySQL**, **MongoDB**
""")

st.markdown("---")

# Contact
st.subheader("📬 Contact & Informations")
st.markdown("""
📧 **Email** : votre.email@example.com  
📞 **Téléphone** : +33 X XX XX XX XX  
🔗 **Réseaux** : [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)  
""")

st.info("N'hésitez pas à me contacter pour toute opportunité ou collaboration.")

# Pied de page
st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
