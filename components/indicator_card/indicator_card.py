from django_components import component


@component.register("indicator_card")
class IndicatorCardComponent(component.Component):
    """Carte indicateur chiffré.

    Args:
        label (str): Intitulé de l'indicateur (ex: "Total facturé").
        value (str): Valeur principale affichée (ex: "7 770 €").
        subtitle (str, optional): Texte secondaire sous la valeur. Par défaut None.
    """
    template_file = "indicator_card.html"

    def get_context_data(self, label, value, subtitle=None):
        return {
            'label': label,
            'value': value,
            'subtitle': subtitle,
        }

    class Media:
        css = "indicator_card.css"
