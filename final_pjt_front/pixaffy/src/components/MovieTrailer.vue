<template>
  <div class="d-block mb-6">
    <vueper-slides bullets-outside :dragging-distance="50" fixed-height="750px">
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

addEventListener("fetch", event => { 
  event.respondWith(async function() {
    // Respond from the cache if we can
    const cachedResponse = await caches.match(event.request);
    if (cachedResponse) return cachedResponse; 
    // Else, use the preloaded response, if it's there 
    const response = await event.preloadResponse;
    if (response) return response;
    // Else try the network. 
    return fetch(event.request);
  }());
});

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
            url: 'https://www.youtube.com/embed/' + this.trailer + '?controls=0&fs=0&modestbranding=1&color=white&iv_load_policy=3&autohide=1&enablejsapi=1',
            props: {
              allow: 'autoplay'
            }
          }
        },
        {
          image: 'https://image.tmdb.org/t/p/w780/' + this.movie.poster_path
        }
      ],
      trailer_key: null,
    }
  },
}
</script>

<style>
  .vueperslide__image {
  transform: scale(0.7);
}
</style>