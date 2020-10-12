from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from app.utils import Util


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'required': 'Please enter your full name.'
                }
            },
            'password': {
                'write_only': True, 'min_length': 8,
                'required': True,
                'error_messages': {
                    'required': 'Please enter a valid password.'
                    }
            },
            'email': {
                'required': True,
                'error_messages': {
                    'required': 'Please enter a valid email address.'
                }
            },
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        token = RefreshToken.for_user(user).access_token
        current_site = '127.0.0.1:8000/api/user/email-verification'
        absurl='http://' + current_site + "?token=" + str(token)
        # Url printed in console
        data={ 'domain': absurl, 'subject': 'Verify Your Email', 'recipient_list': validated_data['email'] }
        Util.send_email(data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Invalid Credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
