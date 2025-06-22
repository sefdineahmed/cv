# app.py
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container
import base64
import datetime

# Configuration de la page
st.set_page_config(
    page_title="Ingénieur Statistique & Informatique Décisionnelle",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# Fonction pour les backgrounds
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background('background.png')  # Décommentez pour utiliser un background personnalisé

# Données du CV
CV_DATA = {
    "nom": "Ingénieur en Statistique et Informatique Décisionnelles",
    "tagline": "Votre expert en données pour des décisions éclairées",
    "apropos": "Je suis un ingénieur spécialisé en analyse de données et modélisation, avec plus de 5 ans d'expérience dans la résolution de problématiques complexes liées aux données. Mon expertise couvre les statistiques appliquées et l'informatique décisionnelle, me permettant de transformer des données brutes en informations stratégiques.",
    "competences": {
        "Analyse de Données": {"niveau": 95, "desc": "Maîtrise de l'analyse multidimensionnelle et multivariée"},
        "Modélisation Prédictive": {"niveau": 90, "desc": "Conception et implémentation de modèles prédictifs"},
        "Programmation": {"niveau": 92, "desc": "R, Python, SAS pour le traitement et l'analyse"},
        "Enquêtes & Questionnaires": {"niveau": 85, "desc": "Conception et traitement rigoureux"},
        "Communication": {"niveau": 88, "desc": "Vulgarisation de résultats complexes"}
    },
    "experiences": [
        {
            "poste": "Prévention de Fraudes Bancaires",
            "description": "Développement de modèles sophistiqués réduisant les pertes financières"
        },
        {
            "poste": "Audit et Évaluation de Risques",
            "description": "Optimisation des stratégies pour entreprises d'assurance"
        },
        {
            "poste": "Encadrement d'Équipe",
            "description": "Gestion d'une équipe de 3 statisticiens juniors"
        },
        {
            "poste": "Rapports Décisionnels",
            "description": "Production de tableaux de bord pour directions générales"
        }
    ],
    "projets": [
        {
            "nom": "Tableau de Bord Interactif",
            "description": "Visualisation des KPIs pour suivi des performances"
        },
        {
            "nom": "Scoring Client (Banque)",
            "description": "Optimisation de l'attribution de crédits et gestion des risques"
        },
        {
            "nom": "Optimisation de Production",
            "description": "Réduction des coûts par simulation statistique"
        },
        {
            "nom": "Étude de Satisfaction Clients",
            "description": "Recommandations stratégiques pour grande enseigne"
        }
    ],
    "formation": [
        {"diplome": "Ingénieur en Statistique", "completion": 100},
        {"diplome": "Analyse Numérique", "completion": 95},
        {"diplome": "Cours Fondamentaux", "completion": 90}
    ],
    "outils": [
        "Python", "R", "SAS", "SQL", "Power BI", 
        "Tableau", "Spark", "Hadoop", "Scikit-learn", "TensorFlow"
    ],
    "contact": {
        "email": "votre.email@example.com",
        "telephone": "+33 X XX XX XX XX",
        "reseaux": ["LinkedIn", "GitHub", "Twitter"]
    }
}

# Animation du header
with st.container():
    colored_header(
        label="",
        description="",
        color_name="blue-70"
    )
    st.markdown(f"<h1 class='main-title'>{CV_DATA['nom']}</h1>", unsafe_allow_html=True)
    st.caption(f"#### {CV_DATA['tagline']}")
    st.markdown("---")

# Navigation
def navigation():
    with st.sidebar:
        st.image("https://cdn.pixabay.com/photo/2017/02/18/11/00/statistic-2076765_960_720.png", width=120)
        st.title("Navigation")
        sections = ["Accueil", "À Propos de Moi", "Compétences Clés", "Expériences Professionnelles", 
                   "Projets Réalisés", "Formation et Diplômes", "Outils et Technologies", "Contact"]
        choice = st.radio("", sections)
        st.markdown("---")
        
        # Widget interactif
        st.subheader("Explorez mon univers")
        tech_filter = st.multiselect("Filtrer par technologie:", CV_DATA["outils"])
        exp_years = st.slider("Années d'expérience:", 1, 10, 5)
        
        # Télécharger CV
        with open("CV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📥 Télécharger mon CV",
            data=PDFbyte,
            file_name="CV_Ingenieur_Data.pdf",
            mime="application/pdf"
        )
    return choice, tech_filter, exp_years

# Sections
def afficher_accueil():
    with st.container():
        cols = st.columns([1,2])
        with cols[0]:
            st.image("https://cdn.pixabay.com/photo/2018/08/14/13/23/ocean-3605547_960_720.jpg", 
                     caption="Transformer les données en valeur")
        with cols[1]:
            with stylable_container(
                key="accueil_box",
                css_styles="""
                {
                    background-color: rgba(13, 17, 23, 0.7);
                    border-radius: 10px;
                    padding: 2rem;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                """
            ):
                st.markdown(f"<h2 style='color: #4FC0E8;'>Bienvenue dans mon portfolio data</h2>", unsafe_allow_html=True)
                st.markdown("""
                <p style='font-size: 18px;'>
                Spécialiste de la transformation des données complexes en stratégies actionnables, 
                je combine expertise technique et vision business pour créer de la valeur.
                </p>
                """, unsafe_allow_html=True)
                
                # Stats interactives
                col_stat = st.columns(3)
                col_stat[0].metric("+ Projets", "50+", "Analytics")
                col_stat[1].metric("Modèles", "120+", "Machine Learning")
                col_stat[2].metric("Efficacité", "35% ↑", "Optimisation")

def afficher_apropos():
    st.header("À Propos de Moi")
    st.write(CV_DATA["apropos"])
    
    # Timeline interactive
    st.subheader("Parcours Professionnel")
    years = [datetime.date.today().year - i for i in range(5,0,-1)]
    for year in years:
        with st.expander(f"🏆 {year} - Réalisations majeures"):
            st.write(f"- Projet innovant en analyse prédictive secteur bancaire")
            st.write(f"- Optimisation processus réduisant les coûts de 15%")
            st.write(f"- Formation d'une équipe de 5 data analysts")

def afficher_competences():
    st.header("Compétences Clés")
    cols = st.columns(2)
    
    for i, (skill, details) in enumerate(CV_DATA["competences"].items()):
        with cols[i%2]:
            with stylable_container(
                key=f"skill_{skill}",
                css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 10px;
                    padding: 1rem;
                    margin-bottom: 1rem;
                    background: linear-gradient(90deg, rgba(79,192,232,0.2) 0%, rgba(79,192,232,0.05) 100%);
                }
                """
            ):
                st.subheader(f"{skill}")
                st.progress(details["niveau"] / 100)
                st.caption(f"{details['niveau']}% - {details['desc']}")

def afficher_experiences(tech_filter):
    st.header("Expériences Professionnelles")
    
    for exp in CV_DATA["experiences"]:
        with st.expander(f"📌 {exp['poste']}", expanded=True):
            st.write(exp["description"])
            if tech_filter:
                st.info(f"Technologies utilisées: {', '.join(tech_filter)}")
            st.button("Voir les détails techniques", key=f"btn_{exp['poste']}")

def afficher_projets():
    st.header("Projets Réalisés")
    
    for projet in CV_DATA["projets"]:
        with stylable_container(
            key=f"projet_{projet['nom']}",
            css_styles="""
            {
                border-radius: 10px;
                padding: 1rem;
                margin: 1rem 0;
                background-color: rgba(30, 50, 70, 0.3);
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
            }
            :hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            """
        ):
            st.subheader(projet["nom"])
            st.write(projet["description"])
            
            # Visualisation interactive
            if "Tableau de Bord" in projet["nom"]:
                chart_data = {"KPI": ["Satisfaction", "Efficacité", "Rentabilité"], "Avant": [60, 65, 70], "Après": [85, 88, 92]}
                st.bar_chart(chart_data, x="KPI")

def afficher_formation():
    st.header("Formation et Diplômes")
    
    for diplome in CV_DATA["formation"]:
        st.subheader(diplome["diplome"])
        st.progress(diplome["completion"] / 100)
        st.caption(f"Complétion: {diplome['completion']}%")

def afficher_outils():
    st.header("Outils et Technologies")
    
    cols = st.columns(4)
    for i, tool in enumerate(CV_DATA["outils"]):
        with cols[i % 4]:
            with stylable_container(
                key=f"tool_{tool}",
                css_styles="""
                {
                    border-radius: 50px;
                    padding: 0.5rem 1rem;
                    margin: 0.5rem;
                    text-align: center;
                    background-color: rgba(79, 192, 232, 0.2);
                }
                """
            ):
                st.markdown(f"**{tool}**")

def afficher_contact():
    st.header("Contact & Informations")
    
    col_contact = st.columns([1,2])
    with col_contact[0]:
        st.subheader("Restons Connectés")
        st.write(f"✉️ {CV_DATA['contact']['email']}")
        st.write(f"📱 {CV_DATA['contact']['telephone']}")
        
        st.subheader("Suivez-moi")
        for res in CV_DATA["contact"]["reseaux"]:
            st.button(f"{res}", use_container_width=True)
    
    with col_contact[1]:
        with st.form(key='contact_form'):
            st.subheader("Envoyez un message")
            name = st.text_input("Nom complet")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit_button = st.form_submit_button(label='Envoyer')
            
            if submit_button:
                st.success("Message envoyé avec succès!")

# Application principale
def main():
    choix, tech_filter, exp_years = navigation()
    
    if choix == "Accueil":
        afficher_accueil()
    elif choix == "À Propos de Moi":
        afficher_apropos()
    elif choix == "Compétences Clés":
        afficher_competences()
    elif choix == "Expériences Professionnelles":
        afficher_experiences(tech_filter)
    elif choix == "Projets Réalisés":
        afficher_projets()
    elif choix == "Formation et Diplômes":
        afficher_formation()
    elif choix == "Outils et Technologies":
        afficher_outils()
    elif choix == "Contact":
        afficher_contact()

if __name__ == "__main__":
    main()
