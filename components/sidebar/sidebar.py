from django_components import component


@component.register("sidebar")
class SidebarComponent(component.Component):
    """Menu latéral principal avec navigation collapse/expand.

    Structure : sidebar fixe à gauche, collapsée par défaut (58px),
    étendue au clic (272px). Accordéon pour les sections avec sous-menus.

    Args:
        active_section (str): Identifiant de la section active
            ('appels', 'messagerie', 'contacts', 'coordonnees',
             'preferences', 'utilisateurs', 'bibliotheque', 'factures').
        user_initials (str, optional): Initiales de l'utilisateur. Défaut 'NV'.
        user_name (str, optional): Nom affiché. Défaut 'N. Vidal'.
        user_role (str, optional): Rôle affiché. Défaut 'Administrateur'.
    """
    template_file = "sidebar.html"

    def get_context_data(
        self,
        active_section="",
        user_initials="NV",
        user_name="N. Vidal",
        user_role="Administrateur",
    ):
        # Sous-sections de "Paramètres de compte"
        settings_subsections = ['coordonnees', 'preferences', 'utilisateurs', 'bibliotheque', 'factures']
        is_settings_active = active_section in settings_subsections

        # Sous-sections de "Appels d'offres"
        appels_subsections = ['appels_nouveaux', 'appels_propositions', 'appels_preselection', 'appels_encours', 'appels_archive', 'appels_corbeille']
        is_appels_active = active_section in appels_subsections or active_section == 'appels'

        return {
            'active_section': active_section,
            'user_initials': user_initials,
            'user_name': user_name,
            'user_role': user_role,
            'is_settings_active': is_settings_active,
            'is_appels_active': is_appels_active,
        }

    class Media:
        css = "sidebar.css"
        js = "sidebar.js"
