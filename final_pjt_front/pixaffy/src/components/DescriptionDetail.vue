<template>
  <div>
    <v-container>
      <v-card>
        <v-row
          class = "mb-6"
          no-gutters
        >
          <v-col
            cols="4"
          >
          <div
            style="
              padding: auto 3px auto;
            "
          >
            <div
              style="
                margin: auto 3px auto;
              "
            >
              <v-img
                :src="posterPath"
              ></v-img>
            </div>
          </div>
          </v-col>
          <v-col
            cols="8"
          >
            <div
              style="
                margin: 5px;
                padding: 10px;
                border-left: 3px solid rgb(218,221,228);
              "
            >
              <div 
                style="font-family: 'Jeju Gothic', sans-serif !important;
                font-size: 40px;
                font-weight: bold;
                margin: 5px 0;
                "
                >{{ movie.title }}
              </div>
              <div
                style="
                  display: flex;
                  font-family: 'Jeju Gothic', sans-serif !important;
                  font-size: 24px;
                  font-weight: bold;
                  margin: 5px 0;
                  color: rgb(90, 96, 120);
                "
              >
                <div 
                  v-for="genre in genres" :key="genre.id"
                  style="margin: auto 5px"
                >
                {{genre.name}}
                </div>
              </div>
              <div
                style="
                  margin-bottom: 10px;
                "
              >
                <v-rating
                    :value="movie.vote_average / 2"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="20"
                  >
                </v-rating>
              </div>
              <h4>{{ movie.overview }}</h4>
            </div>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
    <v-sheet
    class="mx-auto"
    elevation="8"
    max-width="800"
  >
    <v-slide-group
      v-model="model"
      class="pa-4"
      show-arrows
    >
      <v-slide-item
        v-for="actor in actors"
        :key="actor.id"
        v-slot="{ active, toggle }"
      >
        <v-card
          :color="active ? 'rgb(128, 128, 128)' : 'rgb(128, 128, 128)'"
          :img="`https://image.tmdb.org/t/p/w780${actor.profile_path}`"
          class="ma-4"
          height="400"
          width="190"
          @click="toggle"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <v-scale-transition>
              <div
                v-if="active"
                style="color: rgb(255,255,255); font-size: 24px; background-color: rgba(31,41,61,.4);
                padding: 5px 10px;
                border-radius: 10px;
                max-width: 175px;
                text-align: center;
                font-family: 'Jeju Gothic', sans-serif !important;
                "
              >
              {{ actor.original_name }}
              </div>
            </v-scale-transition>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name:'descriptionDetail',
  data: () => ({
      model: null,
      actors: null,
      genres: null,
      selectedActor: null,
    }),
  props: {
    movie: {
      required: true
    }
  },
  computed: {
    posterPath() {
        return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path;
    },
  },
  created() {
    axios({
      url: `https://api.themoviedb.org/3/movie/${this.movie.id}/credits?api_key=c0ea5b6535679915d16aada2f7427157&language=ko-KR`
    })
      .then(res => {
        let casts = []
        for (let person of res.data.cast) {
          if (person.profile_path){
            casts.push(person)
          }
        }
        this.actors = casts
      })
      .catch(err => {
        console.log(err)
      })
    axios({
      url: `https://api.themoviedb.org/3/movie/${this.movie.id}?api_key=c0ea5b6535679915d16aada2f7427157&language=ko-KR`
    })
      .then(res => {
        this.genres = res.data.genres
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>
  .col.col-4 > div {
    margin: auto 3px auto;
  }
</style>