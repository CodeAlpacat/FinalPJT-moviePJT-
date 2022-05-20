<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input
          v-model="credentials.username"
          type="text"
          id="username"
          required
        />
      </div>
      <div>
        <label for="password1">Password: </label>
        <input
          v-model="credentials.password1"
          type="password"
          id="password1"
          required
        />
      </div>
      <div>
        <label for="password2">Password Confirmation:</label>
        <input
          v-model="credentials.password2"
          type="password"
          id="password2"
          required
        />
      </div>
      <!-- <div> -->
        <!-- <v-file-input
          :rules="imageRules"
          @change="findImg"
          ref="profile"
          accept="image/png, image/jpeg, image/bmp"
          placeholder="프로필 이미지를 선택해 주세요"
          prepend-icon="mdi-camera"
          label="프로필 이미지"
        ></v-file-input> -->
        <!-- <label for="profile-image">프로필이미지</label>
        <input
          @change="findImg()"
          type="file"
          ref="profile"
          id="profile-image"
          accept=".png, .jpeg, .bmp"
        />
      </div> -->
      <div>
        {{ this.credentials.profile_img }}
      </div>
      <div>
        <v-text-field
          label="E-mail"
          :rules="emailRules"
          hide-details="auto"
          prepend-icon="mdi-email"
          v-model="credentials.email"
        ></v-text-field>
      </div>
      <div>
        {{ credentials.email }}
      </div>
      <div>
        <v-container fluid>
          <p>{{ genres_list }}</p>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="모험"
                value="12"
                :disabled="countSelectedGenres && !genres_list.includes('12')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="판타지"
                value="14"
                :disabled="countSelectedGenres && !genres_list.includes('14')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="애니메이션"
                value="16"
                :disabled="countSelectedGenres && !genres_list.includes('16')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="드라마"
                value="18"
                :disabled="countSelectedGenres && !genres_list.includes('18')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="공포"
                value="27"
                :disabled="countSelectedGenres && !genres_list.includes('27')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="액션"
                value="28"
                :disabled="countSelectedGenres && !genres_list.includes('28')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="코미디"
                value="35"
                :disabled="countSelectedGenres && !genres_list.includes('35')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="역사"
                value="36"
                :disabled="countSelectedGenres && !genres_list.includes('36')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="서부"
                value="37"
                :disabled="countSelectedGenres && !genres_list.includes('37')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="스릴러"
                value="53"
                :disabled="countSelectedGenres && !genres_list.includes('53')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="범죄"
                value="80"
                :disabled="countSelectedGenres && !genres_list.includes('80')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="다큐멘터리"
                value="99"
                :disabled="countSelectedGenres && !genres_list.includes('99')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="SF"
                value="878"
                :disabled="countSelectedGenres && !genres_list.includes('878')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="미스터리"
                value="9648"
                :disabled="countSelectedGenres && !genres_list.includes('9648')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="음악"
                value="10402"
                :disabled="
                  countSelectedGenres && !genres_list.includes('10402')
                "
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="로맨스"
                value="10749"
                :disabled="
                  countSelectedGenres && !genres_list.includes('10749')
                "
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="가족"
                value="10751"
                :disabled="
                  countSelectedGenres && !genres_list.includes('10751')
                "
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="전쟁"
                value="10752"
                :disabled="
                  countSelectedGenres && !genres_list.includes('10752')
                "
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="genres_list"
                label="TV 영화"
                value="10770"
                :disabled="
                  countSelectedGenres && !genres_list.includes('10770')
                "
              ></v-checkbox>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <div>
        <button>Signup</button>
      </div>
      <div>
        <p>
          {{ credentials.genre_likes }}
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "SignupView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      // formData: {},
      credentials: {
        username: "",
        password1: "",
        password2: "",
        //  장르 추가
        genre_likes: null,
        email: "",
        // profile_img: null,
      },
      genres_list: [],
      // imageRules: [
      //   (value) =>
      //     !value ||
      //     value.size < 2000000 ||
      //     "프로필 이미지 사이즈는 2Mb 보다 작아야 합니다.",
      // ],
      emailRules: [
        (value) =>
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            value
          ) || "이메일 형식을 확인하세요.",
      ],
    };
  },
  computed: {
    ...mapGetters(["authError"]),
    countSelectedGenres() {
      return !(this.genres_list.length < 3);
    },
  },
  methods: {
    ...mapActions(["signup"]),
    // findImg() {
    //   this.credentials.profile_img = this.$refs.profile.files[0];
    // },
    // submitData() {
    //   const formData = new FormData();
    //   formData.append("username", this.credentials.username);
    //   formData.append("password1", this.credentials.password1);
    //   formData.append("password2", this.credentials.password2);
    //   formData.append("genre_likes", this.credentials.genre_likes);
    //   formData.append("email", this.credentials.email);
    //   formData.append("profile_img", this.credentials.profile_img);
    //   for (let key in formData.entries()) {
    //     console.log(`${key}`);
    //   }
    //   this.$http
    //     .post("http://localhost:8000/api/v1/accounts/signup/", formData, {
    //       headers: {
    //         "Content-Type": "multipart/form-data",
    //       },
    //     })
    //     .then((res) => {
    //       console.log(res);
    //     });
    // },
  },
  watch: {
    genres_list: function (val) {
      const new_val = { genre_likes: val };
      this.credentials.genre_likes = JSON.stringify(new_val);
      console.log(this.credentials.genre_likes);
    },
  },
};
</script>

<style></style>
