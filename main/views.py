from django.views import generic

from .models import Game, Company, Person, Platform, Genre, Mode


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class GamesView(generic.ListView):
    template_name = 'main/games.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.all()


class GameView(generic.DetailView):
    model = Game
    template_name = 'main/game.html'

    # def get_queryset(self):
    #     return Game.objects.all()


class CompanyView(generic.DetailView):
    model = Company
    template_name = 'main/company.html'


class PersonView(generic.DetailView):
    model = Person
    template_name = 'main/person.html'


class PlatformView(generic.DetailView):
    model = Platform
    template_name = 'main/platform.html'


class GenreView(generic.DetailView):
    model = Genre
    template_name = 'main/genre.html'


class ModeView(generic.DetailView):
    model = Mode
    template_name = 'main/mode.html'
