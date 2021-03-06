<template>
  <v-hover v-slot="{ hover }" open-delay="100">
    <v-card :elevation="hover ? 16 : 2" :class="{ 'on-hover': hover }">
      <!-- 나중에 url을 디테일 페이지로 or 모달 -->
      <v-img
        :src="posterPath"
        alt="포스터가 없습니다"
        class=""
        @click="dialog = true"
      ></v-img>
      <v-card-title
        class="sutitle-2"
        @click="dialog = true"
        style="cursor: pointer"
        >{{ movieProps.title }}</v-card-title
      >
      <v-card-text>
        <v-row align="center" class="mx-0">
          <v-rating
            :value="movieProps.vote_average / 2"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
          >
          </v-rating>
          <div class="ml-4">
            {{ movieProps.vote_average * 10 }} % | {{ movieProps.release_date }}
          </div>
        </v-row>
        <div class="my-4 subtitle-2">
          <span v-for="(genre, index) in movieProps.genres" :key="genre">
            {{ genretypeName(genre, index) }}
          </span>
        </div>
      </v-card-text>
      <v-dialog v-model="dialog" width="1700">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            text
            color="white"
            style="height: 70px; font-size: 20px"
            v-bind="attrs"
            v-on="on"
            @click="dialog = true"
            >{{ movieProps.title }}</v-btn
          >
        </template>
        <v-card style="background-color: rgb(75, 82, 97)">
          <detail-dialog
            :movieModal="movieProps"
            :profile="profile"
          ></detail-dialog>
          <v-card-actions style="height: 60px">
            <v-spacer></v-spacer>
            <button class="dialog-close" @click="dialog = false">
              <span>Close</span>
            </button>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </v-hover>
</template>

<script>
import DetailDialog from "@/components/DetailDialog.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "CardViewItem",
  components: {
    DetailDialog,
  },
  props: {
    movieProps: {
      required: true,
    },
  },
  data() {
    return {
      genres_list: [],
      dialog: false,
      userId: null,
    };
  },
  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/w500/" + this.movieProps.poster_path;
    },
    ...mapGetters(["profile"]),
  },
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/genres/");
    this.genres_list = await response.json();
    this.username = await JSON.parse(localStorage.getItem("currentUser"))
      .username;
    const payload = { username: this.username };
    await this.fetchProfile(payload);
  },
  methods: {
    ...mapActions(["movieSelect", "fetchProfile", "getMovieTrailer"]),
    genretypeName(id, index) {
      for (const item of this.genres_list) {
        if (item.id == id) {
          if (this.movieProps.genres.length - 1 == index) {
            return item.name;
          } else {
            return item.name + ",";
          }
        }
      }
    },
  },
};
</script>

<style>

.dialog-close {
  width: 120px;
  height: 50px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: #892626;
  text-align: center;
  opacity: 1;
  cursor: pointer;
  transition: 0.5s;
}
.dialog-close:hover {
  opacity: 0.8;
}

.dialog-close span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 20px;
}

.dialog-close span:after {
  content: "\f55a";
  font-family: "Font Awesome 5 Free";
  font-weight: 600;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -40px;
  transition: 0.5s;
}

.dialog-close:hover span {
  padding-right: 25px;
}

.dialog-close:hover span:after {
  opacity: 1;
  right: 0;
}
</style>
