from django_components import component


STATUS_CONFIG = {
    'paid':    {'label': 'Payée',      'css_modifier': 'paid'},
    'pending': {'label': 'En attente', 'css_modifier': 'pending'},
    'overdue': {'label': 'En retard',  'css_modifier': 'overdue'},
}


@component.register("status_tag")
class StatusTagComponent(component.Component):
    """Tag de statut coloré avec pastille.

    Basé sur le pattern _tag.sass du design actuel, avec les couleurs
    de statut définies dans _colors.sass (green, orange, red).

    Args:
        status (str): Clé de statut parmi : 'paid', 'pending', 'overdue'.
        label (str, optional): Texte affiché. Si None, utilise le label par défaut du statut.
    """
    template_file = "status_tag.html"

    def get_context_data(self, status, label=None):
        config = STATUS_CONFIG.get(status, STATUS_CONFIG['pending'])
        return {
            'status': config['css_modifier'],
            'label': label or config['label'],
        }

    class Media:
        css = "status_tag.css"
