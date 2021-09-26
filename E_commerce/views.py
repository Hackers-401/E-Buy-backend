from rest_framework.response import Response
from rest_framework import views,viewsets,generics,mixins
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class ProductView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Product.objects.all().order_by("-id")
    serializer_class=ProductSerializers
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)


class ProfileView(views.APIView):
    authentication_classes=[TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        try:
            query = Profile.objects.get(prouser=request.user)
            serializer = ProfileSerializers(query)
            response_message = {"error":False,"data":serializer.data}
        except:
            response_message = {"error":True,"message":"Somthing is Wrong"}
        return Response(response_message)