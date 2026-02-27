from django_components import component


@component.register("toggle_row")
class ToggleRowComponent(component.Component):
    """Ligne avec label, description et toggle.

    Utilisé pour les paramètres on/off (renouvellement automatique,
    notifications, etc.).

    Args:
        label (str): Intitulé du paramètre.
        label_id (str): ID HTML du label (pour aria-labelledby du switch).
        description (str, optional): Texte explicatif sous le label. Par défaut None.

    Slots:
        toggle: Composant switch ou autre contrôle à droite.
    """
    template_file = "toggle_row.html"

    def get_context_data(self, label, label_id, description=None):
        return {
            'label': label,
            'label_id': label_id,
            'description': description,
        }

    class Media:
        css = "toggle_row.css"
