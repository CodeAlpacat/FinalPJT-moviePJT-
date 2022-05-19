<template>
  <div>
<<<<<<< HEAD
    <v-dialog
      v-model="dialogDetail"
      width="800px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
          @click="toggleDialogDetail"
        >
          Detail
        </v-btn>
      </template>
      <div>
        <card-algorithm></card-algorithm>
      </div>
      <upcoming-movies></upcoming-movies>
      <v-card>
        <detail-dialog :pk="1"></detail-dialog>
      </v-card>
    </v-dialog>
=======
    <div >
      <genre-based-recommendation></genre-based-recommendation>
      <card-view></card-view>
    </div>
>>>>>>> bcb11683ae535ef6940af4beb6438ec516c79eca
  </div>
</template>

<script>
<<<<<<< HEAD
import UpcomingMovies from '@/components/UpcomingMovies.vue';
import CardAlgorithm from '@/components/CardAlgorithm.vue';
import DetailDialog from '@/components/DetailDialog.vue';
import { mapGetters, mapActions } from 'vuex';

=======
import GenreBasedRecommendation from '@/components/GenreBasedRecommendation.vue';
import CardView from '@/components/CardView.vue';
>>>>>>> bcb11683ae535ef6940af4beb6438ec516c79eca
export default {
  name: "HomeView",

  components: {
<<<<<<< HEAD
    UpcomingMovies,
    CardAlgorithm,
    DetailDialog
  },
  computed: {
    ...mapGetters(['dialogDetail'])
=======
    CardView,
    GenreBasedRecommendation
>>>>>>> bcb11683ae535ef6940af4beb6438ec516c79eca
  },

  data() {
    return {
      movies: [],
    };
  },

  methods:{
    ...mapActions(['toggleDialogDetail'])
  },

  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/");
    this.movies = await response.json();
  },


};
</script>

<style>

</style>