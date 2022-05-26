<template>
  <div>
    <h1
      style="
        color: rgb(218, 221, 228);
        font-family: 'Jeju Gothic', sans-serif !important;
        font-size: 64px;
        text-align: center;
        margin-bottom: 50px;
        margin-top: 100px;
        margin-right: 120px;
      "
    >
      모든 영화를 한 눈에!
    </h1>
    <v-container>
      <v-row>
        <v-col
          v-for="movie in movieList"
          :key="movie.title"
          cols="12"
          xs="12"
          sm="6"
          lg="3"
          xl="2"
          style="margin-bottom: 60px; margin-right: 15px; margin-left: 15px"
        >
          <card-movie-view-item
            :movie="movie"
            :profile="profile"
            style="background-color: #1f293c !important"
          ></card-movie-view-item>
        </v-col>
      </v-row>

      <button class="login-card__div__form__btn btn_fixed" @click="more">
        <span>더보기</span>
      </button>
    </v-container>
  </div>
</template>

<script>
import CardMovieViewItem from "@/components/CardMovieViewItem.vue";
import { mapGetters } from "vuex";
import axios from "axios";
export default {
  components: {
    CardMovieViewItem,
  },
  async created() {
    const response = await fetch(
      `http://127.0.0.1:8000/movies/${this.page}/more/`
    );
    this.page += 1;
    this.movieDatas = await response.json();
  },
  computed: {
    ...mapGetters(["profile"]),
    movieList() {
      return this.movieDatas;
    },
  },
  methods: {
    more() {
      axios
        .get(`http://127.0.0.1:8000/movies/${this.page}/more/`)
        .then((res) => {
          for (let i = 0; i < res.data.length; i++) {
            this.movieDatas.push(res.data[i]);
          }
          this.page += 1;
        });
    },
  },
  data() {
    return {
      movieDatas: null,
      page: 0,
    };
  },
};
</script>

<style>
.btn_fixed {
  position: fixed;
  right: 0;
  bottom: 0;
  margin-right: 70px;
  margin-bottom: 70px;
}

.login-card__div__form__btn {
  width: 120px;
  height: 60px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: #892626;
  text-align: center;
  opacity: 1;
  cursor: pointer;
  transition: 0.5s;
  margin-top: 15px;
}
.login-card__div__form__btn:hover {
  opacity: 0.7;
}

.login-card__div__form__btn span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 20px;
}

.login-card__div__form__btn span:after {
  content: "\2b";
  font-size: 30px;
  position: absolute;
  opacity: 0;

  bottom: -5px;
  right: -15px;
  transition: 0.5s;
}

.login-card__div__form__btn:hover span {
  padding-right: 25px;
}

.login-card__div__form__btn:hover span:after {
  opacity: 1;
  right: 0;
}
</style>
