import json
from allauth.account.adapter import DefaultAccountAdapter

#커스텀한 필드의 정보가 실제 데이터베이스에 반영되도록 저장.
class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        profile_img = data.get("profile_img")
        genre_likes = data.get("genre_likes")
        # print('-----------------------------------------')
        # json_genre_likes = json.loads(genre_likes)
        # array_json = json_genre_likes.get("genre_likes")
        # print(array_json)
        if profile_img:
            user.profile_img = genre_likes
        if genre_likes:
            user.genre_likes = genre_likes

        user.save()
        return user