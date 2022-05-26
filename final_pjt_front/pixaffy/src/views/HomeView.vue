<template>
  <div>
      <div 
        id="Live"
        class="player" 
        data-property="{
          videoURL: 'https://youtu.be/lxPSJvEWRvI',
          mute: true,
          showControls: false,
          useOnMobile: true,
          quality: 'highres',
          containment: 'self',
          loop: true,
          autoPlay: true,
          stopMovieOnBlur: false, 
          startAt: 0,
          opacity: 0.7
        }"
        style="
          position: fixed !important;
          width: 271vmax;
          height: 100vmax;
        "
      >
      </div>
    <div class="recommend-text-div">
      <div class="home-text" style="
        color:rgb(221, 147, 48); 
        font-family: 'Jeju Gothic', sans-serif !important; 
        font-size: 64px; 
        position: absolute; 
        top: 20px;
        left: 50%;
        width: 610px;
        transform: translate(-50%, 0)
      ">좋아하는 장르가 있어? </div>
    </div>
    <genre-based-recommendation></genre-based-recommendation>
    <div class="now-playing-text-div">
      <div style="
        color:rgb(218,221, 228); 
        font-family: 'Jeju Gothic', sans-serif !important; 
        font-size: 64px; 
        position: absolute; 
        top: 975px;
        left: 50%;
        width: 510px;
        transform: translate(-50%, 0)
      "> 현재 상영중인 영화 </div>
    </div>
    <card-view :keyword="'nowplaying/'"></card-view>
    <!-- <card-view :keyword="'recommend/' + String(user.pk)"></card-view> -->
    <div class="now-playing-text-div">
      <div style="
        color:rgb(218,221, 228); 
        font-family: 'Jeju Gothic', sans-serif !important; 
        font-size: 64px; 
        position: absolute; 
        top: 1585px;
        left: 50%;
        width: 510px;
        transform: translate(-50%, 0)
      "> 상영 예정인 영화 </div>
    </div>
    <card-view :keyword="'upcoming/'"></card-view>
  </div>
</template>

<script>
import GenreBasedRecommendation from '@/components/GenreBasedRecommendation.vue';
import CardView from '@/components/CardView.vue';
export default {
  name: "HomeView",
  data() {
    return {
      user: null,
    }
  },
  components: {
    CardView,
    GenreBasedRecommendation
  },
  created() {
    // eslint-disable-next-line
    jQuery( function() {
    // eslint-disable-next-line
      jQuery( '#Live' ).YTPlayer();
    });
    this.user = JSON.parse(localStorage.getItem['currentUser'])
  }

};
</script>

<style>
  #Live {
    z-index: -5;
  }

  .inline-YTPlayer {
    position: fixed !important;
    width: 271vmax !important;
    height: 100vmax !important;
    top: -50vmax;
  }

  .YTPOverlay {
    width: 271vmax !important;
    height: 100vmax !important;
  }

  .recommend-text-div {
    height: 120px;
  }

  @media screen and (max-width: 1349px) {

  }

  @media screen and (max-width: 899px) {

  }
</style>