from django_components import component


@component.register("card")
class CardComponent(component.Component):
    """Conteneur générique avec header optionnel.

    Basé sur le pattern list_card du design actuel ($list-card-bg-color).

    Args:
        full_width (bool, optional): Occupe toute la largeur d'une grille. Par défaut False.
        flush (bool, optional): Supprime le padding du body. Par défaut False.
        has_header (bool, optional): Affiche le header. Par défaut True.
        extra_css_class (str, optional): Classe CSS supplémentaire.

    Slots:
        icon: Icône dans le titre du header.
        title: Texte du titre du header.
        header_actions: Boutons d'action dans le header (côté droit).
        body: Contenu principal de la card.
    """
    template_file = "card.html"

    def get_context_data(self, full_width=False, flush=False, has_header=True, extra_css_class=None):
        return {
            'full_width': full_width,
            'flush': flush,
            'has_header': has_header,
            'extra_css_class': extra_css_class,
        }

    class Media:
        css = "card.css"
