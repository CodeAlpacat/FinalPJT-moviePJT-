<template>
  <div>
    <div style="display: flex; align-items: center;" @mouseover='MouseOnComment' @mouseleave='MouseOutComment'>
      <div style="flex-grow: 1">
        <div class="comment-body">
          <div>
            <router-link :to="{ name: 'profile', params: { username:payload.username, profileUser:profile }}" class="router__author">{{ payload.username }}</router-link>
          </div>
          <span style="font-family:'Jeju Gothic', sans-serif !important;">
            {{ payload.content }}
          </span>
        </div>
      </div>
      <div style="flex-basis: 50px; margin-top: 15px;" v-if="isOnMouse"  >
      <!-- v-if에 인증된 사용자인지 확인하는 것도 넣어줄 것 -->
        <v-btn
          color="red darken-4"
          icon
          @click="deleteComment({'articlePk': article.pk, 'commentPk': comment.id ? comment.id : comment.pk })"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "CommentView",
  props: {
    comment: Object,
    articlePk: Number,
    username: {
      required: true
    }
  },
  data(){
    return {
      isOnMouse: false,
      payload: {
        content: this.comment.content,
        username: this.comment.user.username,
      },
    }
  },
  computed: {
    ...mapGetters(['article', 'profile'])
  },
  methods: {
    ...mapActions(['deleteComment', 'fetchProfile']),
    MouseOnComment(){
      this.isOnMouse = true
    },
    MouseOutComment(){
      this.isOnMouse = false
    }
  },
  created() {
    this.fetchProfile({username:this.$route.params.username})
  }
}
</script>

<style>
  .comment-body {
    border-bottom: 1px solid rgb(203,206,213);
    margin-top: 15px;
    padding: 5px;
    font-family:'Jeju Gothic', sans-serif !important;
    font-size: 16px;
  }
  .comment-body > div {
    background-color: rgb(173,192,221);
    font-weight: bold;
    border-radius: 2px;
    font-family:'Jeju Gothic', sans-serif !important;
    margin-bottom: 10px;
    padding: 5px 5px;
    font-size: 20px;
  }

    .router__author {
    color: rgb(2, 7, 21) !important;
    font-weight: bold;
  }
</style>