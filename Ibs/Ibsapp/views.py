from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import generics
# from django.shortcuts import get_list_or_404
# from rest_framework.generics import ListAPIView

from tablib import Dataset
from .models import *
from .serializers import *
from .resources import MemberResource


def simple_upload(request):
    if request.method == 'POST':
        member_resource = MemberResource()
        dataset = Dataset()
        new_members = request.FILES['myfile']

        imported_data = dataset.load(new_members.read())
        result = member_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            member_resource.import_data(dataset, dry_run=False)  # Actually import now

        inventory_resource = InventoryResource()
        dataset = Dataset()
        new_inventory = request.FILES['myfile']


        imported_data = dataset.load(new_inventory.read())
        result = member_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            inventory_resource.import_data(dataset, dry_run=False) 


    return render(request, 'core/simple_upload.html')

# class HotelList(ListAPIView):
#     serializer_class =HotelSerializer
#     queryset = Hotel.objects.all()    
#     lookup_field='id'

# class RoomList(generics.ListAPIView):
#     queryset=Room.objects.all()    
#     serializer_class=RoomSerializer

# class GuestList(generics.ListAPIView):
#     queryset=Guest.objects.all()
#     serializer_class=GuestSerializer

# class BookingList(generics.ListAPIView):
#     queryset=Booking.objects.all()
#     serializer_class=BookingSerializer

# class BookingDetail(ListView):
#     template_id='booking/id.html'

#     def get_queryset(self):
#         self.id =get_object_or_404(Booking, id=self.kwargs['id'])           
#         return Booking.objects.filter(id=self.id) 

@api_view(['GET','POST'])
def api_inventory_list_view(request):
    inventory=Inventory.objects.all()
    if request.method=='GET':
        serializer=InventorySerializer(inventory,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=InventorySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def api_member_list_view(request):
    member=Member.objects.all()
    if request.method=='GET':
        serializer=MemberSerializer(member,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer=MemberSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)                    

@api_view(['GET','POST'])
def api_booking_list_view(request):
    booking=Booking.objects.all()
    if request.method =='GET':
        serializer=BookingSerializer(booking,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def booking_details(request, pk):
    try: 
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist: 
        return Response({'message': 'The booking does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        booking_serializer = BookingSerializer(booking) 
        return Response(booking_serializer.data) 
 
    elif request.method == 'PUT': 
        booking_data = JSONParser().parse(request) 
        booking_serializer = BookingSerializer(booking, data=booking_data) 
        if booking_serializer.is_valid(): 
            booking_serializer.save() 
            return Response(booking_serializer.data) 
        return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        booking.delete() 
        return Response({'message': 'Booking was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

