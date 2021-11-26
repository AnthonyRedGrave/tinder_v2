from .models import Profile, ProfileInformation

def get_profiles_with_opposite_gender(request_user):

    request_user_profile = Profile.objects.get(user=request_user)
    request_user_profile_info = ProfileInformation.objects.get(profile=request_user_profile)

    return Profile.objects.exclude(profile_information__gender = request_user_profile_info.gender), request_user_profile_info

def get_profiles_with_same_favorites(profiles, request_user_profile_info):
    request_user_favorites = request_user_profile_info.favorites.all()
    profiles_with_same_favorites = profiles.filter(profile_information__favorites__in = request_user_favorites)
    count_profiles = profiles_with_same_favorites.count()
    return profiles_with_same_favorites[:count_profiles/2]