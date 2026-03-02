from django_components import component


@component.register("topbar")
class TopbarComponent(component.Component):
    """Barre supérieure avec breadcrumb, recherche et avatar utilisateur.

    Se positionne à droite de la sidebar (margin-left: 58px).
    Sticky en haut de page.

    Args:
        breadcrumb_parent (str, optional): Texte du parent dans le breadcrumb. Défaut 'M2BPO'.
        breadcrumb_current (str): Texte de la page courante dans le breadcrumb.
        user_initials (str, optional): Initiales de l'utilisateur. Défaut 'NV'.
        search_placeholder (str, optional): Placeholder du champ recherche. Défaut 'Rechercher…'.

    Slots:
        actions: Boutons d'action supplémentaires à droite (optionnel).
    """
    template_file = "topbar.html"

    def get_context_data(
        self,
        breadcrumb_parent="M2BPO",
        breadcrumb_current="",
        user_initials="NV",
        search_placeholder="Rechercher…",
    ):
        return {
            'breadcrumb_parent': breadcrumb_parent,
            'breadcrumb_current': breadcrumb_current,
            'user_initials': user_initials,
            'search_placeholder': search_placeholder,
        }

    class Media:
        css = "topbar.css"
