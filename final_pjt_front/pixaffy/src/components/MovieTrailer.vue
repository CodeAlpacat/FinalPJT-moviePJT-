<template>
  <div class="d-block mb-6">
    <vueper-slides bullets-outside :dragging-distance="50">
      <vueper-slide
        v-for="(slide, i) in slides"
        :key="i"
        :image="slide.image"
        :video="slide.video" />
    </vueper-slides>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
export default {
  name: 'movieTrailer',
  props: {
    movie: Object,
    trailer: String,
  },
  components: { VueperSlides, VueperSlide },
  data() {
    return {
      slides: [
        {
          image: 'https://image.tmdb.org/t/p/w780/' + this.movie.poster_path,
          video: {
            url: 'https://www.youtube.com/embed/' + this.trailer,
            props: {
              allow: 'autoplay'
            }
          }
        },
        // {
        //   image: 'https://image.tmdb.org/t/p/w780/' + this.movie.poster_path
        // }
      ]
    }
  },
  computed: {
  },
  created() {

  }
}
</script>

<style>

</style>