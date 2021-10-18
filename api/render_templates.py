def render_template(template_name: str, **context):
    with open(f'templates/{template_name}') as template:
        return template.read().format(**context)
