from persistent import Persistent
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList


class AgentsContainer(PersistentMapping):
    """
    This is the list of agents
    """


class Agent(PersistentMapping):
    """
    This is an agent that connects to cameras
    """
    def __init__(self, name, security_token):
        self.name = name
        self.security_token = security_token



class Camera(Persistent):
    """
    This is an IP Camera. An agent will connect to this camera, so it needs this information to talk to it
    """
    def __init__(self, name, ip_address, username, password, codec, network_protocol, recording, path):
        self.name = name
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.codec = codec
        self.network_protocol = network_protocol
        self.recording = recording
        self.path = path


class Settings(Persistent):
    """
    This contains the settings for the whole server
    """
    def __init__(self, hostname='spionisto'):
        self.hostname = hostname
        self.https_enabled = False
    
    def as_dict(self):
        return self.__dict__.copy()


class SpionistoRoot(PersistentMapping):
    """
    This is the root of the application
    """
    __name__ = None
    __parent__ = None


def appmaker(zodb_root):
    if 'app_root' not in zodb_root:
        app_root = SpionistoRoot()

        # Settings
        settings = Settings()
        settings.__name__ = 'settings'
        settings.__parent__ = app_root
        app_root['settings'] = settings

        # Setup agents container
        agents = AgentsContainer()
        agents.__name__ == 'agents'
        agents.__parent__ == app_root
        app_root['agents'] = agents

        # App root
        zodb_root['app_root'] = app_root
        
    return zodb_root['app_root']
