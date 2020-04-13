from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""
    login_url = reverse_lazy('accounts:login')

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect(reverse_lazy('accounts:login'))
    #     return super().dispatch(request, *args, **kwargs)
