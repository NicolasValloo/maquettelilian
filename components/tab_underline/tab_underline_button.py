from django_components import component


@component.register("tab_underline_button")
class TabUnderlineButtonComponent(component.Component):
    """Bouton individuel pour le composant tab_underline.

    Doit être utilisé à l'intérieur du slot "tabs" d'un tab_underline.
    Utilise le contexte injecté par tab_underline (via {% provide %})
    pour déterminer si l'onglet est actif.

    Args:
        tab_id (str): Identifiant de l'onglet (correspond au panel id="panel-{tab_id}").
        label (str): Texte affiché sur le bouton.
        counter (int, optional): Compteur affiché à côté du label. None = pas de compteur.
    """
    template_file = "tab_underline_button.html"

    def get_context_data(self, tab_id, label, counter=None):
        return {
            'tab_id': tab_id,
            'label': label,
            'counter': counter,
            'use_oob_swap': 'Use-Oob-Swap' in self.request.headers,
        }
