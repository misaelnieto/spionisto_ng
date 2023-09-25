from pyramid.view import view_config
import colander
import deform
from slugify import slugify
from pyramid.httpexceptions import HTTPSeeOther


class CameraSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    name = colander.SchemaNode(colander.String())
    ip_address = colander.SchemaNode(colander.String())
    username = colander.SchemaNode(colander.String())
    password = colander.SchemaNode(colander.String())
    codec = colander.SchemaNode(colander.String())
    network_protocol = colander.SchemaNode(colander.String())
    recording = colander.SchemaNode(colander.Boolean())
    path = colander.SchemaNode(colander.String())


@view_config(name='new_camera', context='..models.Agent',
             renderer='spionisto:templates/camera_edit.pt')
def add_camera(context, request):
    return "New camera"


@view_config(name='edit', context='..models.Camera',
             renderer='spionisto:templates/camera_edit.pt')
def edit_camera(context, request):
    return "Edit camera"


@view_config(name='delete', context='..models.Camera',
             renderer='spionisto:templates/camera_edit.pt')
def delete_camera(context, request):
    return "Delete camera"

