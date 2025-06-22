# Portfolio Data Scientist - Streamlit

Ce projet est une application Streamlit interactive pour présenter un portfolio professionnel d'ingénieur en statistique et informatique décisionnelle. L'application combine créativité, interactivité et professionnalisme pour mettre en valeur les compétences et expériences du candidat.

## Fonctionnalités Clés

- 🎨 Interface moderne avec animations et effets visuels
- 🧭 Navigation intuitive avec sidebar interactive
- 🔍 Filtrage dynamique par technologies et années d'expérience
- 📊 Visualisations interactives pour les projets
- 📝 Formulaire de contact fonctionnel
- 📥 Téléchargement du CV en PDF
- 📱 Design responsive

## Prérequis

- Python 3.8+
- Pip

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/sefdineahmed/portfolio.git
cd portfolio
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Ajoutez votre CV au format PDF dans le dossier principal et nommez-le `CV.pdf`

4. Lancez l'application :
```bash
streamlit run app.py
```

## Structure des Fichiers

```
portfolio/
├── app.py                # Code principal de l'application Streamlit
├── styles.css            # Feuille de style CSS personnalisée
├── requirements.txt      # Dépendances Python
├── CV.pdf                # Votre CV au format PDF (à ajouter)
└── README.md             # Ce fichier d'instructions
```

## Personnalisation

Pour personnaliser le contenu du portfolio, modifiez le dictionnaire `CV_DATA` dans le fichier `app.py` avec vos informations personnelles :

```python
CV_DATA = {
    "nom": "Votre Nom",
    "tagline": "Votre slogan professionnel",
    "apropos": "Votre description personnelle",
    # ... autres sections
}
```

## Dépendances

Les principales dépendances sont :

- `streamlit==1.32.0` - Framework pour l'application web
- `streamlit-extras==0.3.6` - Composants supplémentaires pour Streamlit
- `pandas==2.1.4` - Manipulation des données
- `plotly==5.18.0` - Visualisations interactives

## Fonctionnalités Interactives

- **Filtrage des expériences** par technologies spécifiques
- **Timeline interactive** du parcours professionnel
- **Effets de survol** sur les projets
- **Indicateurs de compétences** animés
- **Visualisation dynamique** des KPIs

## Déploiement

L'application peut être déployée sur :
- Streamlit Cloud
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run

## Contribution

Les contributions sont les bienvenues ! Pour proposer des améliorations :
1. Forkez le projet
2. Créez une nouvelle branche (`git checkout -b feature/amélioration`)
3. Committez vos changements (`git commit -am 'Ajout d'une fonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/amélioration`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Auteur**: Sefdine Ahmed
**Contact**: ahmed.sefdine@uadb.edu.sn
**Date**: 22 juin 2025
