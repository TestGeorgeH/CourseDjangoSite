class TitleMixin:
    title = None

    def get_context_data(self, **kvargs):
        context = super(TitleMixin, self).get_context_data(**kvargs)
        context['title'] = self.title
        return context
