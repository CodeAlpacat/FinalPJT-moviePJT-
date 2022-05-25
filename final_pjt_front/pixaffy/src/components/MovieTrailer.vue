<template>
  <div id="trailer" class="d-block mb-6 ">
    <vueper-slides bullets-outside :dragging-distance="50" fixed-height="750px" class="hidden-sm-and-down">
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
import axios from 'axios';


export default {
  name: 'movieTrailer',
  props: {
    movie: Object,
  },
  components: { VueperSlides, VueperSlide },
  data() {
    
    return {
      trailer: null,
      slides: [
        {
          image: 'https://image.tmdb.org/t/p/w780/' + this.movie.poster_path,
          video: {
            url: null,
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
  computed: {
  },
  created() {
    console.log(this.trailer)
    addEventListener('activate', event => {
      event.waitUntil(async function() {
        // Feature-detect
        if (self.registration.navigationPreload) {
          // Enable navigation preloads!
          await self.registration.navigationPreload.enable();
        }
      }());
    });
    addEventListener('fetch', event => {
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
    axios({
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=c0ea5b6535679915d16aada2f7427157`
      })
        .then(res => {
          this.trailer = res.data.results[0].key
          this.slides[0].video.url = 'https://www.youtube.com/embed/' + res.data.results[0].key
        })
        .catch(error => {
          console.log(error)
        })
}
}
</script>

<style>
  .vueperslide__image {
  transform: scale(0.7);
}
</style>