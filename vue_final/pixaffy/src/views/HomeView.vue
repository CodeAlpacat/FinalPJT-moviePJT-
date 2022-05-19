<template>
  <div>
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
      <upcoming-movies></upcoming-movies>
      <v-card>
        <detail-dialog></detail-dialog>
      </v-card>
    </v-dialog>
    <div >
      <genre-based-recommendation></genre-based-recommendation>
      <card-view></card-view>
    </div>
  </div>
</template>

<script>
import DetailDialog from '@/components/DetailDialog.vue';
import { mapGetters, mapActions } from 'vuex';

import GenreBasedRecommendation from '@/components/GenreBasedRecommendation.vue';
import CardView from '@/components/CardView.vue';
export default {
  name: "HomeView",

  components: {
    DetailDialog,
    CardView,
    GenreBasedRecommendation
  },
  computed: {
    ...mapGetters(['dialogDetail']),
    
  },

  data() {
    return {
      movies: [],
    };
  },

  methods:{
    ...mapActions(['toggleDialogDetail','movieSelect']),
  },

  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/nowplaying");
    this.movies = await response.json();
    
  },


};
</script>

<style>

</style>