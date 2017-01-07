"""
Nuke Actions, commands and functions used in The Foundry Nuke.
"""
from assetbox.base.plugins.actions import BaseAction


class AbcImport(BaseAction):
    """Action to import an Alembic file.

    TODO: update to work properly in Nuke.
    """

    NAME = 'ABC Import'
    FILETYPE = 'abc'

    def execute(self, path, **kwargs):
        """Run the command."""
        if self.valid_filetype(path):
            print path


class ExrImport(BaseAction):
    """Action to import a exr and create a Nuke Read node."""

    name = 'Exr Import'
    filetype = 'exr'

    def execute(self, path, **kwargs):
        """Run the command."""
        if self.valid_filetype(path):
            import nuke
            nuke.nodes.Read(file=str(path))


def register_actions(*args):
    """Register all the actions into the host app."""
    return [AbcImport(), ExrImport()]
