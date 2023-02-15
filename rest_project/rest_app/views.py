import json

from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework import generics,viewsets
from rest_framework import mixins



# Create your views here.
class Todosview(APIView):
    def post(self,request):
        a=TodoSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)

    def get(self,request):
        qs=todos.objects.all()
        a=TodoSerializer(qs,many=True)
        # To view the data, pass the datas into serializer
        # mant=True tells the DRF that querset contains multiple itemsS
        # so def needs to serialize each items using serializer class
        return Response(a.data)

class TodoDetails(APIView):
    def get(self,request,**kwargs):  # **kwargs to get todo_id=1
        id=kwargs.get("todo_id")
        todo=todos.objects.get(id=id)
        a=TodoSerializer(todo)
        return Response(a.data)

    def put(self,request,**kwargs):         #update
        id=kwargs.get("todo_id")
        todo=todos.objects.get(id=id)
        a=TodoSerializer(instance=todo,data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)

    def delete(self,request,**kwargs):
        id=kwargs.get("todo_id")
        todo=todos.objects.get(id=id)
        todo.delete()
        return Response({'msg':'deleted'})


class Mobileview(APIView):
    def post(self,request):
        a=MobileSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)

    def get(self,request):
        qs=Mobile.objects.all()
        a=MobileSerializer(qs,many=True)
        return Response(a.data)

class MobileDetails(APIView):
    def get(self,request,**kwargs):
        id=kwargs.get("mob_id")
        mob=Mobile.objects.get(id=id)
        a=MobileSerializer(mob)
        return Response(a.data)

    def put(self,request,**kwargs):
        id=kwargs.get("mob_id")
        mob=Mobile.objects.get(id=id)
        a=MobileSerializer(instance=mob,data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)

    def delete(self,request,**kwargs):
        id=kwargs.get("mob_id")
        mob=Mobile.objects.get(id=id)
        mob.delete()
        return Response({'msg':'Deleted'})


class UserCreationView(APIView):
    def post(self,request):
        a=UserSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response({"msg":"Registered Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        qs = User.objects.all()
        a = UserSerializer(qs, many=True)
        return Response(a.data)


class SignInView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():                   # DRF, validated.data instead of cleaned.data
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=uname,password=password)
            # authenticate : if the given credentials are valid, it will return a user object.
            if user:        # if true, ie: if that user exists.
                login(request,user)         # login : it is used to assign permission to a specific users.
                return Response({'msg':'Logged in Successfully'})
            else:
                return Response({'msg':'Logged in Failed'})


class MixinList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = MixinSerializer
    queryset = MixinModel.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class MixinDetails(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = MixinSerializer
    queryset = MixinModel.objects.all()
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class EmployeeView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class EmployeeDetails(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class CarView(viewsets.ViewSet):
    serializer_class=CarSerializer
    model=carModel

    def list(self,request):
        a=self.model.objects.all()
        serializer=self.serializer_class(a,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,**kwargs):
        id=kwargs.get("pk")         #pk --> primary key
        todo=self.model.objects.get(id=id)
        serializer=self.serializer_class(data=request.data,instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,**kwargs):
        id=kwargs.get("pk")
        todo=self.model.objects.get(id=id)
        serializer=self.serializer_class(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def destroy(self,request,**kwargs):
        id=kwargs.get("pk")
        todo=self.model.objects.get(id=id)
        todo.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)


class MovieView(viewsets.ViewSet):
    serializer_class=MovieSerializer
    model=MovieModel

    def list(self,request,):
        a = self.model.objects.all()
        serializer = self.serializer_class(a, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,**kwargs):
        id=kwargs.get("pk")
        todo=self.model.objects.get(id=id)
        serializer=self.serializer_class(data=request.data,instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,**kwargs):
        id=kwargs.get("pk")
        todo=self.model.objects.get(id=id)
        serializer=self.serializer_class(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def destroy(self,request,**kwargs):
        id=kwargs.get("pk")
        todo=self.model.objects.get(id=id)
        todo.delete()
        return Response({"msg":"Deleted"},status=status.HTTP_200_OK)


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()


# Interview question - to load a json file to postman
def read_rest():
    # json file path, mode of operation -read,encoding
    with open(r"C:\Users\Sony\PycharmProjects\pythonProject1\restapi\rest_project\rest_app\rest.json","r",encoding="utf8") as f:
        data=json.load(f)      #json.load : The json.load() is a function that takes a file object and it returns a json object
    return data


class rest(APIView):        # without id
    def get(self,request):
        data=read_rest()
        return Response({"data":data},status=status.HTTP_200_OK)


class restDetails(APIView):     # with id
    def get(self,request,**kwargs):
        id=kwargs.get("id")
        data=read_rest()
        try:
            todo=[i for i in data if i["id"]==id][0]
            return Response({"todo":todo},status=status.HTTP_200_OK)
        except:
            return Response({"msg":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)

class MyRest(APIView):
    def get(self,request):
        path=r"C:\Users\Sony\PycharmProjects\pythonProject1\restapi\rest_project\rest_app\rest.json"
        with open(path,'r',encoding="UTF8") as f:
            data=json.load(f)
        return render(request,'index.html',{'data':data})

class MyRestid(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=read_rest()
        todo=[i for i in data if i["id"]==id][0]
        return render(request,'abc.html',{'data':todo})



# #exam
# class RegisterView(APIView):
#     def post(self,request):
#         a=RegSerializer(data=request.data)
#         if a.is_valid():
#             a.save()
#             return Response({"msg":"Registered Successfully"},status=status.HTTP_201_CREATED)
#         else:
#             return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         qs = User.objects.all()
#         a = RegSerializer(qs, many=True)
#         return Response(a.data)
#
#
# class LoginView(APIView):
#     def post(self,request):
#         serializer=LogSerializer(data=request.data)
#         if serializer.is_valid():
#             uname=serializer.validated_data.get("username")
#             password=serializer.validated_data.get("password")
#             user=authenticate(request,username=uname,password=password)
#             if user:
#                 login(request,user)
#                 return Response({'msg':'Login Successful'})
#             else:
#                 return Response({'msg':'Login Failed'})


def read_film():
    with open(r"C:\Users\Sony\PycharmProjects\pythonProject1\restapi\rest_project\rest_app\film.json","r",encoding="utf8") as f:
        data=json.load(f)
    return data

#to fetch all data
class FilmGet(APIView):
    def get(self,request):
        data=read_film()
        return Response({"data":data},status=status.HTTP_200_OK)

#http://127.0.0.1:8000/rest_app/film/

class FilmTitle(APIView):
    def get(self,request):
        title=request.query_params.get("title")
        year=request.query_params.get("year")
        data=read_film()
        a=[i for i in data if (i["Title"]==title)&(i["Year"]==year)]
        return Response({"data":a})

#work
# fetch films from 2015-2019
# user input: year_1=2015
# year_2=2019
#   a=[i for i in data if (i["Year"]>=2015)&(i["Year"]<=2019)]

class FilmFromYear(APIView):
    def get(self,request):
        year1=request.query_params.get("year1")
        year2=request.query_params.get("year2")
        data=read_film()
        a=[i for i in data if (i["Year"]>=year1)&(i["Year"]<=year2)]
        return Response({"data":a})




