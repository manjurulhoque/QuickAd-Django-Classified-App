from django.urls import reverse_lazy


class CustomLoginRequiredMixin:
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(request, *args, **kwargs)
