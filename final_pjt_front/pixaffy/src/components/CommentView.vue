<template>
  <div @mouseover='MouseOnComment' @mouseout='MouseOutComment'>
    <div style="display: flex; align-items: center;">
      <div style="flex-grow: 1">
        <div class="comment-body">
          <div>
            댓글 작성자
          </div>
          댓글 내용
        </div>
      </div>
      <div style="flex-basis: 50px; margin-top: 15px;" v-if="isOnMouse" @mouseout='MouseOutComment' >
        <v-btn
          color="red darken-4"
          icon
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentView",
  data: () => ({
    isOnMouse: false,
  }),
  methods: {
    MouseOnComment(){
      this.isOnMouse = true
    },
    MouseOutComment(){
      this.isOnMouse = false
    }
  }
}
</script>

<style>
  .comment-body {
    border-bottom: 1px solid rgb(203,206,213);
    margin-top: 15px;
    padding: 5px;
  }
  .comment-body > div {
    background-color: rgb(173,192,221);
    font-weight: bold;
    border-radius: 2px;
  }
</style>