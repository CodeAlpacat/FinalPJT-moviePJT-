<template>
  <figure>
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="" />
    <figcaption class="d-flex justify-space-between" style="flex-flow: wrap">
      <!-- 상세페이지로 이동 or 다이얼로그 띄움 -->
      
      <v-dialog v-model="dialog" width="800" scrollable>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text color="white" style="height: 70px; font-size: 20px " v-bind="attrs"
            v-on="on"
            @click="dialog = true">
              <span 
                style="font-family: 'Jeju Gothic', sans-serif !important;"
              >
                {{movie.title}}
              </span>
            </v-btn>
        </template>
        <v-card>
          <detail-dialog :movieModal="movie" :profile="profile"></detail-dialog>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="dialog = false">
              I accept
            </v-btn>
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
import DetailDialog from "@/components/DetailDialog.vue"
import { mapActions, mapGetters } from "vuex";
export default {
  name: 'GenreBasedRecommendationsCard',
  props: {
    movie: {
      required: true,
    },
  },
  components: {
    DetailDialog
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

</style>
