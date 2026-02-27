from django_components import component


@component.register("chip")
class ChipComponent(component.Component):
    """Élément inline léger.

    Affiche une valeur courte dans un badge discret
    (moyen de paiement, catégorie, etc.).

    Args:
        text (str): Texte affiché dans le chip.
    """
    template_file = "chip.html"

    def get_context_data(self, text):
        return {
            'text': text,
        }

    class Media:
        css = "chip.css"
