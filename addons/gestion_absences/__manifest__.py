{
    'name': 'Gestion des absences et justifications',
    'version': '1.0',
    'summary': 'Gestion des absences des étudiants',
    'category': 'Ce module permet de gérer les absences et justifications',
    'author': 'BENCHAOU SALMA',
    'depends': ['base'],
    'data': [
    'views/absence_view.xml',
    'views/justification_view.xml',
    'views/etudiant_view.xml', 
    'views/menu.xml',          
],
    'installable': True,
    'application': True,
}
