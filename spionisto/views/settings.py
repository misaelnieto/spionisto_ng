from pyramid.view import view_config
import colander
import deform.widget


class SettingsPage(colander.MappingSchema):
    hostname = colander.SchemaNode(colander.String())
    https_enabled = colander.SchemaNode(colander.Boolean())


@view_config(context='..models.Settings', renderer='spionisto:templates/settings.jinja2')
def view_settings(context, request):
    schema = SettingsPage()
    settings_form =  deform.Form(schema, buttons=('Save',))

    if 'submit' in request.params:
        controls = request.POST.items()
        try:
            validated = settings_form.validate(controls)
        except deform.ValidationFailure as e:
            return {'form': e.render()}

        # Change the content and redirect to the view
        context.hostname = validated['hostname']
        context.https_enabled = validated['https_enabled']

    return {'form': settings_form.render(context.as_dict())}

