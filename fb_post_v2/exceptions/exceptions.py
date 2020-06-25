class InvalidUserException(Exception):
    pass


class InvalidCommentException(Exception):
    pass

class InvalidPostException(Exception):
    pass

class ReactionDoesNotExist(Exception):
    pass

class PermissionDenied(Exception):
    pass