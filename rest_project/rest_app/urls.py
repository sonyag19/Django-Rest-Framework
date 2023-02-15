from django.urls import path
from rest_app import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("vCar",views.CarView,basename="vCar")
router.register("Movie",views.MovieView,basename="Movie")
router.register("Person",views.PersonView,basename="Person")

urlpatterns=[
    path('first/',views.Todosview.as_view()),
    # as_view() --> It is a  function that is used to connect your class and url.
    path('first/<int:todo_id>',views.TodoDetails.as_view()),

    path('second/',views.Mobileview.as_view()),
    path('second/<int:mob_id>',views.MobileDetails.as_view()),

    path('signIn/',views.UserCreationView.as_view()),
    path('login/',views.SignInView.as_view()),

    path('mixin/',views.MixinList.as_view()),
    path('mixin/<int:id>',views.MixinDetails.as_view()),

    path('Employee/',views.EmployeeView.as_view()),
    path('Employee/<int:id>',views.EmployeeDetails.as_view()),

    # path('Register/',views.RegisterView.as_view()),
    # path('Loginnew/',views.LoginView.as_view())

    path('rest/',views.rest.as_view()),
    path('rest/<int:id>',views.restDetails.as_view()),
    path('Myrestfrontend/',views.MyRest.as_view()),
    path('MyrestfrontendID/<int:id>',views.MyRestid.as_view()),

    path('film/',views.FilmGet.as_view()),
    path('filmTitle/',views.FilmTitle.as_view()),
    path('filmFromYear/',views.FilmFromYear.as_view())

]+(router.urls)