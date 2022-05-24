<template>
  <div>
    <div style="display: flex; align-items: center;" @mouseover='MouseOnComment' @mouseleave='MouseOutComment'>
      <div style="flex-grow: 1">
        <div class="comment-body">
          <div>
            <router-link :to="{ name: 'profile', params: { username:payload.username }}" class="router__author">{{ payload.username }}</router-link>
          </div>
          <span style="font-family:'Jeju Gothic', sans-serif !important;">
            {{ payload.content }}
          </span>
        </div>
      </div>
      <div style="flex-basis: 50px; margin-top: 15px;" v-if="(isOnMouse && (payload.username === currentUser.username))"  >
      <!-- 댓글 작성자와 현재 사용자가 일치하고, onMouse이면 삭제버튼 활성화 -->
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
        username: this.comment.user.username, // 코멘트 작성자
      },
      currentUser: JSON.parse(localStorage.getItem("currentUser")) // 현재 로그인한 사용자
    }
  },
  computed: {
    ...mapGetters(['article',])
  },
  methods: {
    ...mapActions(['deleteComment']),
    MouseOnComment(){
      this.isOnMouse = true
    },
    MouseOutComment(){
      this.isOnMouse = false
    }
  },
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