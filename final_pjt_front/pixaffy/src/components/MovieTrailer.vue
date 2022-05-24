<template>
  <div class="d-block mb-6" v-if="isVideo">
    <vueper-slides bullets-outside :dragging-distance="50">
      <vueper-slide
        v-for="(slide, i) in slides"
        :key="i"
        :image="slide.image" />
    </vueper-slides>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'movieTrailer',
  props: {
    movie: Object,
  },
  data() {
    return {
      slides: [
        {
          image: 'https://image.tmdb.org/t/p/w780/' + this.movie.poster_path,
          video: {
            url: this.videoUrl,
            props: {
              allow: 'autoplay;'
            }
          }
        },
        {
          image: 'https://image.tmdb.org/t/p/w780/' + this.movie.poster_path
        }
      ]
    }
  },
  computed: {
    ...mapGetters([
      'isVideo',
      'videoUrl',
    ])
  },
  created() {

  }
}
</script>

<style>

</style>