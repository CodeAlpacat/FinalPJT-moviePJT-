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
          quality: 'hd2160',
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
    <div style="margin-top: 80px" data-aos="fade-left" data-aos-duration="2000">
      <div class="now-playing-text-div d-flex justify-center mb-0">
        <div
          style="
            z-index: 99;
            color: rgb(218, 221, 228);
            font-family: 'Jeju Gothic', sans-serif !important;
            font-size: 64px;
            width: 700px;
          "
        >
          지금 볼 수 있는 영화는?
        </div>
      </div>
      <card-view
        :keyword="'http://127.0.0.1:8000/movies/nowplaying/'"
        :is_api="false"
      ></card-view>
    </div>
    <div style="margin-top: 80px" data-aos="fade-left" data-aos-duration="2000">
      <div class="now-playing-text-div d-flex justify-center mb-0">
        <div
          style="
            z-index: 99;
            color: rgb(218, 221, 228);
            font-family: 'Jeju Gothic', sans-serif !important;
            font-size: 64px;
            width: 700px;
          "
        >
          이런 영화들이 유명해요!
        </div>
      </div>
      <card-view
        :keyword="'https://api.themoviedb.org/3/movie/popular?api_key=c0ea5b6535679915d16aada2f7427157&language=ko-KR&page=1'"
        :is_api="true"
      ></card-view>
    </div>
    <div style="margin-top: 80px" data-aos="fade-left" data-aos-duration="2000">
      <div class="now-playing-text-div d-flex justify-center mb-0">
        <div
          style="
            z-index: 99;
            color: rgb(218, 221, 228);
            font-family: 'Jeju Gothic', sans-serif !important;
            font-size: 64px;
            width: 700px;
          "
        >
          평점 높은건 어떠세요?
        </div>
      </div>
      <card-view
        :keyword="'https://api.themoviedb.org/3/movie/popular?api_key=c0ea5b6535679915d16aada2f7427157&language=ko-KR&page=1'"
        :is_api="true"
      ></card-view>
    </div>
    <div style="margin-top: 80px" data-aos="fade-left">
      <div class="now-playing-text-div d-flex justify-center mb-0">
        <div
          style="
            z-index: 99;
            color: rgb(218, 221, 228);
            font-family: 'Jeju Gothic', sans-serif !important;
            font-size: 64px;
            width: 700px;
            padding-left: 50px;
          "
        >
          이제 곧 상영 한다구요!
        </div>
      </div>
      <card-view
        :keyword="'http://127.0.0.1:8000/movies/upcoming/'"
        :is_api="false"
      >
      </card-view>
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
    this.user = JSON.parse(localStorage.getItem("currentUser"));
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
  left: 0px;
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
