from djangorestframework.views import ListOrCreateModelView
from djangorestframework.permissions import IsUserOrIsAnonReadOnly

class AuthListOrCreateView(ListOrCreateModelView):
    permissions = (IsUserOrIsAnonReadOnly, )