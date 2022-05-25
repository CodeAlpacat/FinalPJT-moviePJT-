<template>
  <div class="animate__fadeOut">
  <v-sheet
    class="mx-auto"
    elevation="8"
    max-width="800"
    style="
      background-color: rgb(51,56,66)
    "
  >
    <v-slide-group
      v-model="model"
      class="pa-4"
      show-arrows
    >
      <v-slide-item
        v-for="movie in movies"
        :key="movie.id"
        v-slot="{ active, toggle }"
      >
        <v-card
          :img="`https://image.tmdb.org/t/p/w780/${movie.poster_path}`"
          :color="active ? 'rgb(128, 128, 128)' : 'rgb(128, 128, 128)'"
          class="ma-4"
          height="400"
          width="183"
          @click="toggle"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <v-scale-transition>
              <!-- <v-icon
                v-if="active"
                color="white"
                size="48"
                v-text="'mdi-close-circle-outline'"
              ></v-icon> -->
            </v-scale-transition>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
  </div>
</template>

<script>
export default {
  name:'overviewDetail',
  data: () => ({
    model: null,
  }),
  props: {
    movies: Array
  },

}
</script>

<style>

</style>