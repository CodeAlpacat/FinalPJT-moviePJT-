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
      style="position: fixed !important; width: 2560px; height: 1440px"
    ></div>
    <genre-based-recommendation></genre-based-recommendation>
    <div style="margin-top: 80px">
      <div class="now-playing-text-div d-flex justify-center mb-0">
        <div
          style="
            z-index: 99;
            color: rgb(218, 221, 228);
            font-family: 'Jeju Gothic', sans-serif !important;
            font-size: 64px;
            width: 510px;
          "
        >
          현재 상영중인 영화
        </div>
      </div>
      <card-view :keyword="'nowplaying/'"></card-view>
    </div>
    <!-- <card-view :keyword="'recommend/' + String(user.pk)"></card-view> -->
    <div style="margin-top: 80px">
      <div class="now-playing-text-div d-flex justify-center mb-0">
        <div
          style="
            z-index: 99;
            color: rgb(218, 221, 228);
            font-family: 'Jeju Gothic', sans-serif !important;
            font-size: 64px;
            width: 510px;
            padding-left: 50px;
          "
        >
          상영 예정 영화
        </div>
      </div>
      <card-view :keyword="'upcoming/'"> </card-view>
    </div>
  </div>
</template>

<script>
import GenreBasedRecommendation from "@/components/GenreBasedRecommendation.vue";
import CardView from "@/components/CardView.vue";
export default {
  name: "HomeView",
  data() {
    return {
      user: null,
    };
  },
  components: {
    CardView,
    GenreBasedRecommendation,
  },
  mounted() {
    // eslint-disable-next-line
    jQuery(function () {
      // eslint-disable-next-line
      jQuery("#Live").YTPlayer();
    });
    this.user = JSON.parse(localStorage.getItem('currentUser'))
  },

};
</script>

<style>
#Live {
  z-index: -5;
}

.inline-YTPlayer {
  position: fixed !important;
  width: 2560px !important;
  height: 1440px !important;
  top: -200px;
  left: -512px;
}

.YTPOverlay {
  width: 2560px !important;
  height: 1440px !important;
}

.recommend-text-div {
  height: 120px;
}

@media screen and (max-width: 1349px) {
}

@media screen and (max-width: 899px) {
}
</style>
