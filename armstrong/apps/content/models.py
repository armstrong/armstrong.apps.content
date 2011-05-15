from armstrong.core.arm_content.models import ContentBase


class Content(ContentBase):
    """
    Provides a concrete base for the ``ContentBase`` class.

    This adds no additional functionality other than being non-abstract.  This
    creates a ``content_content`` database table that cna be used for queries
    across all of its sub-types.

    *Note*:  This does not provide any admin interfaces.  It is expected that
    this is sub-classed and that the admin is controlled via the various
    specific model instances.
    """
    pass
