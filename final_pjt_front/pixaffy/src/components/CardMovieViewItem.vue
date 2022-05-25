<template>
  <div class="border-rad shadow-card">
    <v-hover>
      <template v-slot:default="{ hover }">
        <v-card
          class="mx-auto border-rad"
          max-width="344"
          height="440"
          style="border-radius: 15px"
        >
          <v-dialog v-model="dialog" width="1700" scrollable>
            <v-card>
              <detail-dialog
                :movieModal="movie"
                :profile="profile"
              ></detail-dialog>
              <v-card-actions style="height: 60px">
                <v-spacer></v-spacer>
                <button class="dialog-close" @click="dialog = false">
                  <span>Close</span>
                </button>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-img height="250" :src="posterPath" class="border-rad-img"></v-img>
          <div style="position: relative">
            <div style="position: absolute; margin-top: 138px">
              <v-card-title>
                <v-rating
                  :value="movie.vote_average / 2"
                  dense
                  color="orange"
                  background-color="orange"
                  hover
                  size="18"
                  class="mr-2"
                ></v-rating>
                <span class="text-subtitle-2 mt-3"
                  >{{ movie.vote_average * 10 }} % |
                  {{ movie.release_date }}</span
                >
              </v-card-title>
            </div>
            <div>
              <v-card-text>
                <h2 class="text-h6">{{ movie.title }}</h2>
                {{
                  movie.overview.length > 50
                    ? movie.overview.substring(0, 50) + "..."
                    : movie.overview
                }}
              </v-card-text>
            </div>
          </div>

          <v-fade-transition>
            <v-overlay v-if="hover" absolute color="#036358">
              <v-btn @click="dialog = true">See more info</v-btn>
            </v-overlay>
          </v-fade-transition>
        </v-card>
      </template>
    </v-hover>
  </div>
</template>

<script>
import DetailDialog from "@/components/DetailDialog.vue";
export default {
  name: "CardMovieViewItem",
  components: {
    DetailDialog,
  },
  computed: {
    posterPath() {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`;
    },
  },
  props: {
    movie: {
      required: true,
    },
    profile: {
      required: true,
    },
  },
  data() {
    return {
      overlay: false,
      dialog: false,
    };
  },
};
</script>

<style>
.border-rad {
  border-radius: 15px;
  background-color: rgba(255, 255, 255, 0.1) !important;
  color: rgba(223, 220, 221, 0.8) !important;
}

.border-rad-img {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}
.shadow-card {
  transition: 0.5s;
}
.shadow-card div:hover {
  box-shadow: -4px 4px 10px rgb(233, 213, 109);
}

.back-color {
  height: 200px;
  border-radius: 15px;
}

.dialog-close {
  width: 120px;
  height: 50px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: #892626;
  text-align: center;
  opacity: 1;
  cursor: pointer;
  transition: 0.5s;
}
.dialog-close:hover {
  opacity: 0.8;
}

.dialog-close span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 20px;
}

.dialog-close span:after {
  content: "\f55a";
   font-family: "Font Awesome 5 Free";
   font-weight: 600;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -40px;
  transition: 0.5s;
}

.dialog-close:hover span {
  padding-right: 25px;
}

.dialog-close:hover span:after {
  opacity: 1;
  right: 0;
}
</style>
