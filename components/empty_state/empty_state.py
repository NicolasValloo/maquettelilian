from django_components import component


@component.register("empty_state")
class EmptyStateComponent(component.Component):
    """Message d'état vide ou d'erreur.

    Affiche une icône, un message, et optionnellement un bouton d'action.
    Utilisé dans les tables vides, les panels sans données, etc.

    Args:
        icon (str, optional): Nom de l'icône SVG à afficher. Par défaut None.
        message (str): Texte du message.
        variant (str, optional): Variante visuelle ('error' pour état erreur). Par défaut None.

    Slots:
        action: Bouton ou lien d'action (ex: "Réessayer").
    """
    template_file = "empty_state.html"

    def get_context_data(self, message, icon=None, variant=None):
        return {
            'icon': icon,
            'message': message,
            'variant': variant,
        }

    class Media:
        css = "empty_state.css"
