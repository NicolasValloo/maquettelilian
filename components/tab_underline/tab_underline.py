from django_components import component


@component.register("tab_underline")
class TabUnderlineComponent(component.Component):
    """Composant pour un ensemble d'onglets avec indicateur underline.

    Variante visuelle du tab_wrapper existant : même logique de navigation,
    mais avec un style underline au lieu du style "background card".

    Args:
        tab_wrapper_id (str): Identifiant HTML unique du wrapper d'onglets.
        active_tab (str): Identifiant de l'onglet actif par défaut.
        aria_label (str, optional): Label ARIA pour le tablist. Par défaut "Onglets".

    Slots:
        tab_wrapper_htmx_attrs: Attributs htmx supplémentaires sur le wrapper.
        tabs: Contenu des boutons d'onglets (tab_underline_button).
    """
    template_file = "tab_underline.html"

    def get_context_data(self, tab_wrapper_id, active_tab, aria_label="Onglets"):
        return {
            'tab_wrapper_id': tab_wrapper_id,
            'active_tab': active_tab,
            'aria_label': aria_label,
        }

    class Media:
        css = "tab_underline.css"
        js = "tab_underline.js"
