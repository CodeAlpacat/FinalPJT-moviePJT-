<template>
  <div>
    <h1>MOvIE 페이지</h1>
    <v-container>
      <v-row>
        <v-col
          v-for="movie in movieDatas"
          :key="movie.id"
          cols="12"
          xs="12"
          sm="6"
          lg="3"
          xl="2"
          style="margin-bottom: 30px"
        >
          <card-movie-view-item
            :movie="movie"
            :profile="profile"
          ></card-movie-view-item>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CardMovieViewItem from "@/components/CardMovieViewItem.vue";
import { mapGetters } from "vuex";
export default {
  components: {
    CardMovieViewItem,
  },
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/nowplaying/");
    this.movieDatas = await response.json();
  },
  computed: {
    ...mapGetters(["profile"]),
  },
  data() {
    return {
      movieDatas: null,
    };
  },
};
</script>

<style></style>
