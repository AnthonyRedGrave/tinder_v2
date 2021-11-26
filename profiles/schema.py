from favorites.models import Favorites
import graphene
from graphene_django import DjangoObjectType
from .models import Language, Profile, ProfileInformation
from .services import get_profiles_with_opposite_gender, get_profiles_with_same_favorites


class LanguageType(DjangoObjectType):
    class Meta:
        model = Language
        fields = ('title',)


class FavoritesType(DjangoObjectType):
    class Meta:
        model = Favorites
        fields = ('title',)


class ProfileInformationType(DjangoObjectType):
    class Meta:
        model = ProfileInformation
        fields = ('gender', 'education', 'weight', 'description', 'location', 'favorites', 'registration_date')
    
    languages = graphene.List(LanguageType)
    favorites = graphene.List(FavoritesType)

    def resolve_languages(self, info):
        return self.languages.all()

    def resolve_favorites(self, info):
        return self.favorites.all()

    


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('id', 'status')
    
    username = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    information = graphene.Field(ProfileInformationType)


    def resolve_username(self, info):
        return self.user.username
    
    def resolve_firstname(self, info):
        return self.user.first_name

    def resolve_lastname(self, info):
        return self.user.last_name

    def resolve_information(self, info):
        return self.profile_information
    

class Query(graphene.ObjectType):
    profiles = graphene.List(ProfileType)
    profiles_with_favorites = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, id=graphene.Int())

    def resolve_profiles(self, info):
        profiles = get_profiles_with_opposite_gender(info.context.user)
        return profiles

    def resolve_profiles_with_favorites(self, info):
        profiles, profile_information = get_profiles_with_opposite_gender(info.context.user)
        profiles_with_favorites = get_profiles_with_same_favorites(profiles, profile_information)
        return profiles_with_favorites

    def resolve_profile(self, info, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)