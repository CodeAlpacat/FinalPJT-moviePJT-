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
            <v-img
              :src="posterPath"
            ></v-img>
          </v-col>
          <v-col
            cols="8"
          >
            <h2>{{ movie.title }}</h2>
            <h4>장르</h4>
            <v-rating
                :value="movie.vote_average / 2"
                color="amber"
                dense
                half-increments
                readonly
                size="20"
              >
            </v-rating>
            <h4>{{ movie.overview }}</h4>
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
      active-class="success"
      show-arrows
    >
      <v-slide-item
        v-for="n in 15"
        :key="n"
        v-slot="{ active, toggle }"
      >
        <v-card
          :color="active ? undefined : 'grey lighten-1'"
          class="ma-4"
          height="200"
          width="100"
          @click="toggle"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <v-scale-transition>
              <v-icon
                v-if="active"
                color="white"
                size="48"
                v-text="'mdi-close-circle-outline'"
              ></v-icon>
            </v-scale-transition>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name:'descriptionDetail',
  data: () => ({
      model: null,
    }),
  computed: {
    ...mapGetters(['movie']),
    posterPath() {
        return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path;
    },
  },
}
</script>

<style>

</style>