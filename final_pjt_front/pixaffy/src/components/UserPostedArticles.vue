<template>
  <v-card
    shaped
    hover
    color="#BBDEFB"
    height="200"
    @click="reveal2 = !reveal2"
    style="box-shadow: 2px -2px 10px"
  >
    <v-card-text>
      <p class="text-h4 text--primary">{{ article.title }}</p>
      <div class="text-h6">작성 시각: {{ new Date(article.created_at) }}</div>
      <div class="text-h6">수정 시각: {{ new Date(article.updated_at) }}</div>
      <div class="text-h6">좋아요 수: {{ article.liked_users.length }}</div>
    </v-card-text>

    <v-expand-transition>
      <v-card
        v-if="reveal2"
        color="#BBDEFB"
        class="transition-fast-in-fast-out v-card--reveal"
        style="height: 100%"
      >
        <v-card-text class="pb-0 text-absolute-card">
          <p class="text-h4 text--primary">
            {{ article.title }}
          </p>
          <p class="text-h6">
            {{ article.content }}
          </p>
          <button class="profile__div1__follow_btn">
            <router-link
              :to="{
                name: 'article',
                params: {
                  article: article,
                  articlePk: article.pk,
                  isLiked: !!likedArticleList.includes(article.pk),
                  articleComments: article.comments,
                  user: article.user,
                },
              }"
            >
              <span>바로가기</span></router-link
            >
          </button>
        </v-card-text>
      </v-card>
    </v-expand-transition>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "UserPostedArticles",
  computed: {
    ...mapGetters(["articles", "likedArticleList"]),
  },
  props:{
    article: {
      required: true
    }
  },
  data() {
    return {
      reveal: false,
      reveal2: false,
    };
  },
  created() {
    console.log(this.article)
  }
};
</script>

<style></style>
