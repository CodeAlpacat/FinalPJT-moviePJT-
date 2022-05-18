<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input  v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div>
        <label for="password1">Password: </label>
        <input v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <label for="password2">Password Confirmation:</label>
        <input v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <v-container fluid>
          <p>{{ credentials.genres }}</p>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="모험"
                value='12'
                :disabled="countSelectedGenres&&!credentials.genres.includes('12')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="판타지"
                value='14'
                :disabled="countSelectedGenres&&!credentials.genres.includes('14')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="애니메이션"
                value='16'
                :disabled="countSelectedGenres&&!credentials.genres.includes('16')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="드라마"
                value='18'
                :disabled="countSelectedGenres&&!credentials.genres.includes('18')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="공포"
                value='27'
                :disabled="countSelectedGenres&&!credentials.genres.includes('27')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="액션"
                value='28'
                :disabled="countSelectedGenres&&!credentials.genres.includes('28')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="코미디"
                value='35'
                :disabled="countSelectedGenres&&!credentials.genres.includes('35')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="역사"
                value='36'
                :disabled="countSelectedGenres&&!credentials.genres.includes('36')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="서부"
                value='37'
                :disabled="countSelectedGenres&&!credentials.genres.includes('37')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="스릴러"
                value='53'
                :disabled="countSelectedGenres&&!credentials.genres.includes('53')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="범죄"
                value='80'
                :disabled="countSelectedGenres&&!credentials.genres.includes('80')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="다큐멘터리"
                value='99'
                :disabled="countSelectedGenres&&!credentials.genres.includes('99')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="SF"
                value='878'
                :disabled="countSelectedGenres&&!credentials.genres.includes('878')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="미스터리"
                value='9648'
                :disabled="countSelectedGenres&&!credentials.genres.includes('9648')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="음악"
                value='10402'
                :disabled="countSelectedGenres&&!credentials.genres.includes('10402')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="로맨스"
                value='10749'
                :disabled="countSelectedGenres&&!credentials.genres.includes('10749')"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="가족"
                value='10751'
                :disabled="countSelectedGenres&&!credentials.genres.includes('10751')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="전쟁"
                value='10752'
                :disabled="countSelectedGenres&&!credentials.genres.includes('10752')"
              ></v-checkbox>
            </v-col>
            <v-col cols="3">
              <v-checkbox
                v-model="credentials.genres"
                label="TV 영화"
                value='10770'
                :disabled="countSelectedGenres&&!credentials.genres.includes('10770')"
              ></v-checkbox>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          //  장르 추가
          genres: [],
        },
      }
    },
    computed: {
      ...mapGetters(['authError']),
      countSelectedGenres() {
        return !(this.credentials.genres.length < 3)
      }
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
