from pyramid.view import view_config
import colander
import deform
from slugify import slugify
from pyramid.httpexceptions import HTTPSeeOther

from ..models import Agent


class AgentSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    security_token = colander.SchemaNode(colander.String())



@view_config(name='add', context='..models.AgentsContainer',
             renderer='spionisto:templates/agent_edit.pt')
def add_agent(context, request):
    schema = AgentSchema()
    agent_form =  deform.Form(schema, buttons=('Save',))

    if 'submit' in request.params:
        controls = request.POST.items()
        try:
            validated = agent_form.validate(controls)
        except deform.ValidationFailure as e:
            return {'form': e.render()}

        agent = Agent(validated['name'], validated['security_token'])
        agent.__parent__ = context
        slug = slugify(agent.name)
        agent.__name__= slug
        context[slug] = agent
        return HTTPSeeOther(location=request.resource_url(agent))

    return {'form': agent_form.render()}



@view_config(name='edit', context='..models.Agent',
             renderer='spionisto:templates/agent_edit.pt')
def edit_agent(context, request):
    schema = AgentSchema()
    agent_form =  deform.Form(schema, buttons=('Save',))

    if 'submit' in request.params:
        controls = request.POST.items()
        try:
            validated = agent_form.validate(controls)
        except deform.ValidationFailure as e:
            return {'form': e.render()}

        agent = Agent(validated['name'], validated['security_token'])
        agent.__parent__ = context
        slug = slugify(agent.name)
        agent.__name__= slug
        context[slug] = agent
        return HTTPSeeOther(location=request.resource_url(agent))

    return {'form': agent_form.render()}



@view_config(name='delete', context='..models.Agent',
             renderer='spionisto:templates/agent_delete.pt')
def edit_agent(context, request):
    agent_form =  deform.Form(colander.Schema(), buttons=('Yes, delete it', 'Cancel'))

    if 'submit' in request.params:
        controls = request.POST.items()
        # TODO: Validate "Yes, delete it"
        parent = context.__parent__
        del parent[context.__name__]
        return HTTPSeeOther(location=request.resource_url(parent))

    return {'form': agent_form.render()}

