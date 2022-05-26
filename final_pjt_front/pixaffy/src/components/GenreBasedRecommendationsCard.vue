<template>
  <figure>
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="" />
    <figcaption class="d-flex justify-space-between" style="flex-flow: wrap">
      <!-- 상세페이지로 이동 or 다이얼로그 띄움 -->

      <v-dialog v-model="dialog" width="1700" scrollable>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            text
            color="white"
            style="height: 70px; font-size: 20px"
            v-bind="attrs"
            v-on="on"
            @click="dialog = true"
          >
            <span style="font-family: 'Jeju Gothic', sans-serif !important">
              {{ movie.title }}
            </span>
          </v-btn>
        </template>
        <v-card>
          <detail-dialog :movieModal="movie" :profile="profile"></detail-dialog>
          <v-card-actions style="height: 60px">
            <v-spacer></v-spacer>
            <button class="dialog-close" @click="dialog = false">
              <span>Close</span>
            </button>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-rating
        class="mt-5"
        :value="movie.vote_average / 2"
        color="amber"
        dense
        half-increments
        readonly
        size="20"
      >
      </v-rating>
    </figcaption>
  </figure>
</template>

<script>
import DetailDialog from "@/components/DetailDialog.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "GenreBasedRecommendationsCard",
  props: {
    movie: {
      required: true,
    },
  },
  components: {
    DetailDialog,
  },
  data() {
    return {
      dialog: false,
      username: null,
    };
  },
  created() {
    this.username = JSON.parse(localStorage.getItem("currentUser")).username;
    const payload = { username: this.username };
    this.fetchProfile(payload);
  },

  computed: {
    ...mapGetters(["profile"]),
  },
  methods: {
    ...mapActions(["fetchProfile"]),
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
