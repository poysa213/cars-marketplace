from rest_framework import serializers


from .models import CarModel, CarImage, CarMarket, Car, Part, PartCategory, PartImage
from users.serializers import UserSerializer



class CarMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarket
        fields = ['id', 'title']

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'title', 'market']


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']

    def create(self, validated_data):
        car_id = self.context.get('car_id')
        return CarImage.objects.create(car_id=car_id, **validated_data)



class PostCarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, required=False)
    class Meta:
        model = Car
        fields = ['id', 'images', 'price', 'market', 'model', 'state', 'transmission', 'date', 'year', 'vitess', 'seats']

        def create(self, validated_data):
            user = self.context.get('user', '')
            if user.is_authenticated:
                car_images = validated_data.pop('images', [])
                car = Car.objects.create(seller=user, **validated_data)
                for image in car_images:
                    car_image = CarImage.objects.create(car=car, image=image)
                    car_image.save()
                return car
            raise serializers.ValidationError(
                {"message": "You must login!"}
            )


class CarSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    images = CarImageSerializer(many=True, required=False)
    class Meta:
        model = Car
        fields = ['id', 'images', 'price', 'market', 'model', 'state', 'transmission', 'date', 'year', 'vitess', 'seats', 'seller']
    
    
    
class PartCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartCategory
        fields = ['id', 'name']

class PartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']

    def create(self, validated_data):
        car_id = self.context.get('car_id')
        return CarImage.objects.create(car_id=car_id, **validated_data)


class PartSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    class Meta:
        model = Part
        fields = ['id', 'seller', 'category', 'price', 'is_verify', 'date', 'state', 'market', 'model']


class PostPartSerializer(serializers.ModelSerializer):
    images = PartImageSerializer(many=True, required=False)
    category_id = serializers.IntegerField()
    class Meta:
        model = Part
        fields = ['category_id', 'price', 'date', 'market', 'model', 'images']

    def create(self, validated_data):
        user = self.context.get('user', '')
        category_id = validated_data.pop('category_id', None)
        category = PartCategory.objects.get(id=category_id)
        # raise serializers.ValidationError({"message": "E"})
        if user.is_authenticated :
            if category is not None:
                part_images = validated_data.pop('images', [])
                part = Part.objects.create(seller=user, category=category, **validated_data)
                for image in part_images:
                    part_image = PartImage.objects.create(part=part, image=image)
                    part_image.save()
                return part
            else:
                msg = {"message": "Enter a valid id category"}
        else:
             msg = {"message": "You must login!"}
            
        raise serializers.ValidationError(msg)
    
class PartCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartCategory
        fields = ['id', 'name']