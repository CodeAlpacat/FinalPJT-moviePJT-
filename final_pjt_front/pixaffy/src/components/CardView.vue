<template>
  <div>
    <h2 class="mt-2" style='color:#E5EAEE;'>Now Playing</h2>
    <v-container fluid>
      <v-row>
        <v-col cols="12" sm="3" lg="2" v-for="movie in movieDatas" :key="movie.id">
          <card-view-item :movieProps="movie"></card-view-item>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CardViewItem from './CardViewItem.vue'
export default {
  name: 'CardAlgorithm',
  components: {
    CardViewItem,
  },
  data() {
    return {
      movieDatas: []
    }
  },
  methods: {
  },
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/nowplaying/");
    this.movieDatas = await response.json()
  }
}
</script>

<style>

</style>