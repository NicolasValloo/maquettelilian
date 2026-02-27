from django_components import component


@component.register("filter_bar")
class FilterBarComponent(component.Component):
    """Barre de filtres horizontale.

    Les filtres (selects) sont à gauche, les actions (boutons) à droite,
    séparés par un spacer flex.

    Slots:
        filters: Contenu des filtres (selects, inputs).
        actions: Boutons d'action (export, ajout, etc.).
    """
    template_file = "filter_bar.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "filter_bar.css"
