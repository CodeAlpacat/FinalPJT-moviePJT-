<template>
  <div>
    <div style="display: flex; align-items: center;" @mouseover='MouseOnComment' @mouseleave='MouseOutComment'>
      <div style="flex-grow: 1">
        <div class="comment-body">
          <div>
            {{ payload.username }}
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
    ...mapGetters(['article'])
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
  created() {
    console.log(this.articlePk)
    console.log(this.article)
    console.log(this.article.pk)
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
</style>