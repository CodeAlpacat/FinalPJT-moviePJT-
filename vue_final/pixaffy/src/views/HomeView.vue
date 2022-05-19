<template>
  <div>
    <div >
      <genre-based-recommendation></genre-based-recommendation>
      <card-view></card-view>
    </div>
  </div>
</template>

<script>
import GenreBasedRecommendation from '@/components/GenreBasedRecommendation.vue';
import CardView from '@/components/CardView.vue';
export default {
  name: "HomeView",

  components: {
    CardView,
    GenreBasedRecommendation
  },

  data() {
    return {
      movies: [],
    };
  },

  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/");
    this.movies = await response.json();
  },
};
</script>

<style>

</style>