from django_components import component


@component.register("information_row")
class InformationRowComponent(component.Component):
    """Paire label/valeur horizontale.

    Utilisé dans les cards pour afficher des données structurées
    (coordonnées, informations de facturation, etc.).

    Args:
        label (str): Intitulé de la donnée.
        subtitle (str, optional): Texte secondaire sous la valeur. Par défaut None.

    Slots:
        value: Contenu de la valeur (texte, HTML, composants).
    """
    template_file = "information_row.html"

    def get_context_data(self, label, subtitle=None):
        return {
            'label': label,
            'subtitle': subtitle,
        }

    class Media:
        css = "information_row.css"
