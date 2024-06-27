from rest_framework import serializers
from .models import Klass, Mehmonxona, Travel




class KlassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Klass().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance



class MehmonxonaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    darajasi = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Mehmonxona().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.darajasi = validated_data.get('darajasi', instance.darajasi)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    

class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    descriptions = serializers.CharField()
    muddati = serializers.CharField()
    price = serializers.IntegerField()
    klass = serializers.CharField()
    mehmonxona = serializers.CharField()

    def create(self, validated_data):
        return Travel().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.descriptions = validated_data.get('descriptions', instance.descriptions)
        instance.muddati = validated_data.get('muddati', instance.muddati)
        instance.price = validated_data.get('price', instance.price)
        instance.klass = validated_data.get('klass', instance.klass)
        instance.mehmonxona = validated_data.get('mehmonxona', instance.mehmonxona)
        instance.save()
        return instance



